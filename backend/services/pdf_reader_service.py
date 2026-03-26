# backend/services/pdf_reader_service.py
import io
import fitz  # PyMuPDF

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Reads PDF bytes and returns the extracted text."""
    # Open the PDF directly from the byte stream
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    
    for page in doc:
        # get_text() is usually much smarter about natural spacing
        extracted = page.get_text()
        if extracted:
            text += extracted + "\n"
            
    return text