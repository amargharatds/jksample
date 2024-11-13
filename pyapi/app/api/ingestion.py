from fastapi import APIRouter, Depends
from app.models import DocumentIngestRequest
from app.database import get_db
from app.crud import insert_embedding
from app.services import generate_embedding

router = APIRouter()

@router.post("/ingest/")
async def ingest_document(request: DocumentIngestRequest, db=Depends(get_db)):
    embedding = await generate_embedding(request.content)
    await insert_embedding(db, request.document_id, embedding, request.content)
    return {"message": "Document ingested successfully."}
