from app.services.flowise_service import FlowiseService


class ChatService:

    def __init__(self):
        self.flowise = FlowiseService()

    def ask(self, question: str, user_id: str):
        return self.flowise.ask_question(question, user_id)