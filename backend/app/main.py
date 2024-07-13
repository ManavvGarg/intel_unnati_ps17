from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from typing import List, Dict
from fastapi.responses import JSONResponse
from services import contract_parser, text_comparer
from services.summarizer import Summarizer
from services.text_classifier import TextClassifier
from services.named_entity_recognition import NamedEntityRecognizer
import tempfile

app = FastAPI()

class Entity(BaseModel):
    entity_group: str
    score: float
    word: str
    start: int
    end: int

class Classification(BaseModel):
    label: str
    score: float

class Result(BaseModel):
    deviations: dict
    original_entities: List[Entity]
    modified_entities: List[Entity]
    original_summary: str
    modified_summary: str
    original_classification: Classification
    modified_classification: Classification

@app.post("/parse/")
async def parse_contract(file: UploadFile = File(...)):
    content = await file.read()
    parsed_data = contract_parser.parse(content)
    return JSONResponse(content={"parsed_data": parsed_data})


@app.post("/compare/", response_model=Result)
async def compare_documents(original_file: UploadFile = File(...), modified_file: UploadFile = File(...), template_file: UploadFile = File(None)):
    # Save uploaded files to temporary locations
    with tempfile.NamedTemporaryFile(delete=False) as temp_original:
        temp_original.write(original_file.file.read())
        temp_original_path = temp_original.name

    with tempfile.NamedTemporaryFile(delete=False) as temp_modified:
        temp_modified.write(modified_file.file.read())
        temp_modified_path = temp_modified.name

    template_path = None
    if template_file:
        with tempfile.NamedTemporaryFile(delete=False) as temp_template:
            temp_template.write(template_file.file.read())
            template_path = temp_template.name

    # Initialize services
    summarizer = Summarizer()
    text_classifier = TextClassifier()
    ner = NamedEntityRecognizer()

    # Parse the documents
    original_text = contract_parser.parse(temp_original_path)
    modified_text = contract_parser.parse(temp_modified_path)
    template_text = contract_parser.parse(template_path) if template_path else None

    # Perform NER, summarization, and classification
    original_entities = ner.recognize(contract_parser.read_file(temp_original_path))
    print(type(original_entities))
    modified_entities = ner.recognize(contract_parser.read_file(temp_modified_path))
    print(type(modified_entities))
    original_summary = summarizer.summarize(temp_original_path)
    modified_summary = summarizer.summarize(temp_modified_path)
    original_classification = text_classifier.classify(temp_original_path)
    modified_classification = text_classifier.classify(temp_modified_path)

    # Compare documents
    deviations = text_comparer.compare(contract_parser.read_file(temp_original_path), contract_parser.read_file(temp_modified_path), contract_parser.read_file(template_path))

    print(original_text)

    print(modified_text)

    print("---------------------------------------------------")
    print(deviations)
    print("---------------------------------------------------")

    # Compile results
    result = {
        "deviations": deviations,
        "original_entities": original_entities,
        "modified_entities": modified_entities,
        "original_summary": original_summary,
        "modified_summary": modified_summary,
        "original_classification": original_classification,
        "modified_classification": modified_classification,
    }

    # result = {
    #     "deviations": deviations,
    #     "original_summary": original_summary,
    #     "modified_summary": modified_summary,
    #     "original_classification": original_classification,
    #     "modified_classification": modified_classification,
    # }

    return result
