import json
import requests

from app.config.settings import settings


class FlowiseService:

    def __init__(self):
        self.base_url = settings.FLOWISE_BASE_URL
        self.api_key = settings.FLOWISE_API_KEY
        self.chatflow_id = settings.FLOWISE_CHATFLOW_ID
        self.document_store_id = settings.FLOWISE_DOCUMENT_STORE_ID

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}"
        }

    def ask_question(self, question: str, user_id: str):

        url = f"{self.base_url}/api/v1/prediction/{self.chatflow_id}"

        payload = {
            "question": question,
            "overrideConfig": {
                "sessionId": user_id
            }
        }

        response = requests.post(
            url,
            headers={
                **self.get_headers(),
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        if "text" in data:
            return data["text"]

        if "answer" in data:
            return data["answer"]

        return json.dumps(data)