from fastapi import APIRouter, UploadFile, File

from app.models.upload_response import UploadResponse
from app.services.upload_service import UploadService

router = APIRouter(
    prefix="/api/upload",
    tags=["Upload"]
)

service = UploadService()


@router.post("", response_model=UploadResponse)
async def upload(file: UploadFile = File(...)):

    result = await service.upload_pdf(file)

    return UploadResponse(
        status="success",
        message="Document uploaded successfully.",
        fileId=result.get("id")
    )