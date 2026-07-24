import os
import requests

from fastapi import UploadFile

from app.config.settings import settings


class UploadService:

    def __init__(self):
        self.upload_url = settings.FLOWISE_UPLOAD_URL
        self.api_key = settings.FLOWISE_API_KEY
        self.doc_id = settings.FLOWISE_DOC_ID

        os.makedirs("uploads", exist_ok=True)

    async def upload_pdf(self, file: UploadFile):

        # Save locally
        local_path = os.path.join("uploads", file.filename)

        with open(local_path, "wb") as f:
            f.write(await file.read())

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        files = {
            "files": (
                file.filename,
                open(local_path, "rb"),
                "application/pdf"
            )
        }

        data = {
            "docId": self.doc_id
        }

        response = requests.post(
            self.upload_url,
            headers=headers,
            files=files,
            data=data,
            timeout=300
        )

        files["files"][1].close()

        if response.status_code >= 400:
            raise Exception(response.text)

        return response.json()