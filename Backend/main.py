# backend/main.py
from fastapi import FastAPI
from api.endpoints import example

app = FastAPI(title="DS POC API")

# Include routes
app.include_router(example.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "API is running"}

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}