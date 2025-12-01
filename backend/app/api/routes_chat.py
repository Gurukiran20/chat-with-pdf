from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import chat_with_pdf

router = APIRouter(prefix="/api", tags=["chat"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str


@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """
    Chat with the PDFs that have been uploaded & indexed.
    """
    answer = chat_with_pdf(req.message)
    return ChatResponse(answer=answer)
