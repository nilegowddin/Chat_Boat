from fastapi import APIRouter

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"]
)

chat_service = ChatService()


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = chat_service.ask(
        request.question,
        request.userId
    )

    return ChatResponse(answer=answer)