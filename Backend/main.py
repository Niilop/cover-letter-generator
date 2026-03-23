from fastapi import FastAPI

app = FastAPI(title="DS POC API")

@app.get("/")
def root():
    return {"message": "DS POC API is running"}