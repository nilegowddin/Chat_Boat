from fastapi import APIRouter, UploadFile, File

from app.models.upload_response import UploadResponse

router = APIRouter(
    prefix="/api/upload",
    tags=["Upload"]
)


@router.post("", response_model=UploadResponse)
async def upload(file: UploadFile = File(...)):

    return UploadResponse(
        status="success",
        message=f"{file.filename} received successfully.",
        fileId="TEMP123"
    )