from langchain_core.prompts import PromptTemplate

def get_cover_letter_prompt() -> PromptTemplate:
    return PromptTemplate.from_template(
        """
You are an expert career coach and copywriter. 
I am going to provide you with my parsed resume text and a job description. 
Please write a professional, engaging, and tailored cover letter that highlights how my experience aligns with the job requirements.

Job Description:
{job_description}

My Resume:
{resume_text}

Cover Letter:
"""
    )

def get_resume_parser_prompt() -> PromptTemplate:
    return PromptTemplate.from_template(
        """
You are an expert resume parser.

Extract structured information from the following resume text.

Return ONLY valid JSON with this structure:
{{
  "name": "...",
  "summary": "...",
  "skills": ["...", "..."],
  "experience": [
    {{
      "role": "...",
      "company": "...",
      "summary": "..."
    }}
  ],
  "education": [
    {{
      "degree": "...",
      "institution": "..."
    }}
  ]
}}

Resume:
{text}
"""
    )


def get_summary_prompt() -> PromptTemplate:
    return PromptTemplate.from_template(
        "You are a helpful assistant. Please summarize the following text concisely:\n\n{text}"
    )