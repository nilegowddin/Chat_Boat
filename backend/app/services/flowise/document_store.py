import json

from fastapi import UploadFile

from app.config.settings import settings
from app.services.flowise.client import flowise_client


class DocumentStore:

    async def upload(self, file: UploadFile):

        content = await file.read()

        files = {
            "files": (
                file.filename,
                content,
                file.content_type
            )
        }

        data = {

            

            "loaderName": file.filename,

            "splitter": json.dumps({
                "config": {
                    "chunkSize": 2000,
                    "chunkOverlap": 200
                }
            }),

            "metadata":json.dumps({}),

            "replaceExisting": True,

            "createNewDocStore": False
        }

        response = await flowise_client.post_multipart(

            endpoint=f"/document-store/upsert/{settings.FLOWISE_DOCUMENT_STORE_ID}",

            files=files,

            data=data

        )

        await file.seek(0)

        return response


document_store = DocumentStore()