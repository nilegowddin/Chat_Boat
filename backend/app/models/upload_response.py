from pydantic import BaseModel


class UploadResponse(BaseModel):
    status: str
    message: str
    fileId: str | None = None