# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy only backend folder contents into /app
COPY ./backend /app

# Install dependencies (adjust if you have requirements.txt)
RUN pip install fastapi uvicorn

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]