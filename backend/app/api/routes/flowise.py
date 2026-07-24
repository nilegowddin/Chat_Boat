from fastapi import APIRouter, HTTPException

from app.services.flowise.client import flowise_client
from app.services.flowise.exceptions import (
    FlowiseAuthenticationError,
    FlowiseAPIError,
)

router = APIRouter(prefix="/flowise", tags=["Flowise"])


@router.get("/status")
async def flowise_status():

    try:
        result = await flowise_client.get("/document-store")

        return {
            "success": True,
            "message": "Connected to Flowise",
            "data": result,
        }

    except FlowiseAuthenticationError as e:
        raise HTTPException(status_code=401, detail=str(e))

    except FlowiseAPIError as e:
        raise HTTPException(status_code=500, detail=str(e))