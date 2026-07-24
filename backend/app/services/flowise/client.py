import json
import requests

from fastapi import UploadFile
from app.config.settings import settings


class FlowiseClient:

    def upload_document(self, file: UploadFile):

        api_url = (
            f"{settings.FLOWISE_BASE_URL}/document-store/upsert/"
            f"{settings.FLOWISE_DOCUMENT_STORE_ID}"
        )

        headers = {
            "Authorization": f"Bearer {settings.FLOWISE_API_KEY}"
        }

        # Reset file pointer
        file.file.seek(0)

        files = {
            "files": (
                file.filename,
                file.file,
                file.content_type or "application/pdf"
            )
        }

        body = {
            # REMOVE THIS IF YOU ARE UPLOADING A NEW DOCUMENT
            # "docId": settings.FLOWISE_DOC_ID,

            "metadata": json.dumps({}),
            "replaceExisting": "false",
            "createNewDocStore": "false",
            "loaderName": "PDF Loader",

            "splitter": json.dumps({
                "config": {
                    "chunkSize": 2000,
                    "chunkOverlap": 200
                }
            })
        }

        print("\n========== FLOWISE REQUEST ==========")
        print("URL:", api_url)
        print("Headers:", headers)
        print("Body:", body)
        print("Filename:", file.filename)
        print("=====================================\n")

        response = requests.post(
            api_url,
            headers=headers,
            files=files,
            data=body,
            timeout=120
        )

        print("\n========== FLOWISE RESPONSE ==========")
        print("Status:", response.status_code)
        print("Body:", response.text)
        print("======================================\n")

        # Don't raise exception yet.
        # Return the response so we can inspect it.
        return {
            "status": response.status_code,
            "body": response.text
        }


flowise_client = FlowiseClient()