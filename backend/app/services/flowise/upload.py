from fastapi import UploadFile


class FlowiseUploadService:

    async def upload_document(
        self,
        file: UploadFile
    ):

        print("Uploading to Flowise...")

        return {
            "documentId": "temporary-id"
        }


flowise_upload_service = FlowiseUploadService()