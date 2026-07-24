from fastapi import APIRouter

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse

router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"]
)


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = f"You asked: {request.question}"

    return ChatResponse(answer=answer)