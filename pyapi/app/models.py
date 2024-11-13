from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class DocumentIngestRequest(BaseModel):
    document_id: UUID
    content: str

class QARequest(BaseModel):
    question: str
    document_ids: Optional[List[UUID]] = None

class QASessionResponse(BaseModel):
    answer: str
