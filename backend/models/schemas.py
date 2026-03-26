from pydantic import BaseModel
from typing import List, Optional
# backend/models/schemas.py
from pydantic import BaseModel

class ExampleRequest(BaseModel):
    name: str
    task: str

class ExampleResponse(BaseModel):
    result: str

# NEW AI Models
class SummaryRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str

class ResumeExtraction(BaseModel):
    name: str
    skills: List[str]
    education: List[str]
    job_experience: str
    brief_summary: str

class ExtractedTextResponse(BaseModel):
    text: str

class CoverLetterRequest(BaseModel):
    resume_text: str
    job_description: str

class CoverLetterResponse(BaseModel):
    cover_letter: str