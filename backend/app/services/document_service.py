from fastapi import UploadFile

from app.services.flowise.client import flowise_client


class DocumentService:

    async def upload(self, file: UploadFile):

        if not file.filename:
            raise Exception("Filename is missing")

        return flowise_client.upload_document(file)


document_service = DocumentService()