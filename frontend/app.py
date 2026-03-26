# frontend/app.py
import streamlit as st
import requests

st.title("Cover Letter Generator 📄")

job_desc = st.text_area("1. Paste the Job Description")

st.write("2. Provide your Resume")
input_method = st.radio("Choose Input Method", ["Upload PDF", "Paste Text Manually"])

# Initialize session state for resume text so it persists between re-runs
if "resume_text" not in st.session_state:
    st.session_state["resume_text"] = ""

if input_method == "Upload PDF":
    uploaded_file = st.file_uploader("Upload your CV (PDF)", type=["pdf"])
    
    if uploaded_file is not None:
        if st.button("Extract Text from PDF"):
            with st.spinner("Extracting text..."):
                url = "http://backend:8000/document/extract-text"
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                
                response = requests.post(url, files=files)
                if response.status_code == 200:
                    st.session_state["resume_text"] = response.json()["text"]
                    st.success("Text extracted successfully! You can review or edit it below.")
                else:
                    st.error("Failed to extract text.")

# Provide a text area for the user to review/edit the extracted text (or paste it directly)
resume_text = st.text_area("Resume Text (Review and Edit)", value=st.session_state["resume_text"], height=200)

if st.button("3. Generate Cover Letter"):
    if resume_text and job_desc:
        with st.spinner("Writing your cover letter..."):
            url = "http://backend:8000/llm/generate-cover-letter"
            payload = {
                "resume_text": resume_text,
                "job_description": job_desc
            }
            
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                st.success("Done!")
                st.write(response.json()["cover_letter"])
            else:
                st.error("Failed to generate cover letter.")
    else:
        st.warning("Please provide both the resume text and the job description.")