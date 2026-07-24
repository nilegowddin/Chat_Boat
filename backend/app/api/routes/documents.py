from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

from app.schemas.common import ApiResponse
from app.services.document_service import document_service

router = APIRouter()


@router.post("/upload")

async def upload(

    file: UploadFile = File(...)

):

    result = await document_service.upload(file)

    return ApiResponse(

        success=True,

        message="Uploaded successfully",

        data=result

    )