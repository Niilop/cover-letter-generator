# tests/test_cover_letter.py
import requests

# Import the mock data from the new file
# (This assumes you are running the script from the root of your project)
from mock_data import mock_resume, mock_job

url = "http://127.0.0.1:8000/llm/generate-cover-letter"

payload = {
    "resume_text": mock_resume,
    "job_description": mock_job
}

print("Sending request to generate cover letter...")
try:
    response = requests.post(url, json=payload)

    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print("\n*** Generated Cover Letter ***\n")
        print(response.json()["cover_letter"])
        print("\n******************************\n")
    else:
        print(f"Error: {response.text}")

except requests.exceptions.ConnectionError:
    print("Connection Error: Make sure your FastAPI backend is running!")