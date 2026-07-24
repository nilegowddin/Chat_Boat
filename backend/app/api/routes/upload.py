from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.upload_service import upload_service

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_document(
    file: UploadFile = File(...)
):

    await upload_service.validate(file)

    return {
        "success": True,
        "filename": file.filename
    }