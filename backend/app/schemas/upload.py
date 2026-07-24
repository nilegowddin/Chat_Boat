from pydantic import BaseModel


class UploadData(BaseModel):
    document_id: str
    file_name: str