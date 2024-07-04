from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from services import contract_parser, text_comparer

app = FastAPI()

@app.post("/parse/")
async def parse_contract(file: UploadFile = File(...)):
    content = await file.read()
    parsed_data = contract_parser.parse(content)
    return JSONResponse(content={"parsed_data": parsed_data})

@app.post("/compare/")
async def compare_documents(original_file: UploadFile = File(...), modified_file: UploadFile = File(...), template_file: UploadFile = File(None)):
    original_content = await original_file.read()
    modified_content = await modified_file.read()
    template_content = await template_file.read() if template_file else None
    
    original_parsed = contract_parser.parse(original_content)
    modified_parsed = contract_parser.parse(modified_content)
    template_parsed = contract_parser.parse(template_content) if template_content else None

    deviations = text_comparer.compare(original_parsed, modified_parsed, template_parsed)
    return JSONResponse(content={"deviations": deviations})
