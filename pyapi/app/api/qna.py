from fastapi import APIRouter, Depends
from app.models import QARequest, QASessionResponse
from app.database import get_db
from app.crud import fetch_relevant_embeddings
from app.services import retrieve_answer

router = APIRouter()

@router.post("/qna/", response_model=QASessionResponse)
async def answer_question(request: QARequest, db=Depends(get_db)):
    embeddings_data = await fetch_relevant_embeddings(db, request.document_ids)
    embeddings = [data['embedding'] for data in embeddings_data]
    texts = [data['content'] for data in embeddings_data]
    answer = await retrieve_answer(request.question, embeddings, texts)
    return QASessionResponse(answer=answer)
