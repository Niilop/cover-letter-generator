# frontend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy only frontend folder contents into /app
COPY ./frontend /app

RUN pip install streamlit

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]