from fastapi import APIRouter, UploadFile, File, HTTPException
from models.schemas import ExtractedTextResponse
from services.pdf_reader_service import extract_text_from_pdf

router = APIRouter(prefix="/document", tags=["Document Processing"])

@router.post("/extract-text", response_model=ExtractedTextResponse)
async def extract_text(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    try:
        file_bytes = await file.read()
        text = extract_text_from_pdf(file_bytes)
        return ExtractedTextResponse(text=text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))