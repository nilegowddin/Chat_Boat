from pydantic import BaseModel


class UploadResponse(BaseModel):

    documentId: str | None = None

    message: str