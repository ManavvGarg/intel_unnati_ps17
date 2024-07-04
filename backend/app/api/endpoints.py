from fastapi import APIRouter, UploadFile, File
from services.contract_parser import ContractParser
from services.text_comparer import TextComparer
from services.summarizer import Summarizer
from services.text_classifier import TextClassifier
from services.named_entity_recognition import NamedEntityRecognizer
import tempfile

router = APIRouter()

@router.post("/compare/")
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
    contract_parser = ContractParser()
    text_comparer = TextComparer()
    summarizer = Summarizer()
    text_classifier = TextClassifier()
    ner = NamedEntityRecognizer()

    # Parse the documents
    original_text = contract_parser.parse(temp_original_path)
    modified_text = contract_parser.parse(temp_modified_path)
    template_text = contract_parser.parse(template_path) if template_path else None

    # Perform NER, summarization, and classification
    original_entities = ner.recognize(original_text)
    modified_entities = ner.recognize(modified_text)
    original_summary = summarizer.summarize(original_text)
    modified_summary = summarizer.summarize(modified_text)
    original_classification = text_classifier.classify(original_text)
    modified_classification = text_classifier.classify(modified_text)

    # Compare documents
    deviations = text_comparer.compare(original_text, modified_text, template_text)

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

    return result
