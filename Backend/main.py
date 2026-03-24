# backend/main.py
from fastapi import FastAPI
from fastapi import Depends
from api.endpoints import example
from core.config import Settings, get_settings

app = FastAPI(title="DS POC API")

# Include routes
app.include_router(example.router)

# Root endpoint
@app.get("/")
def root(settings: Settings = Depends(get_settings)):
    return {"message": f"{settings.app_name} is running"}

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return {"uptime": "todo", "requests": 0}