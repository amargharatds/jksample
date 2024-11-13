from fastapi import FastAPI
from app.api import ingestion, qna, selection

app = FastAPI()

app.include_router(ingestion.router, prefix="/api/v1")
app.include_router(qna.router, prefix="/api/v1")
app.include_router(selection.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the RAG-based Q&A API"}
