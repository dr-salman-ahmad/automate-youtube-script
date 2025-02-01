from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()


class TranscribeRequest(BaseModel):
    url: str


@router.post("/transcribe")
async def transcribe(request: TranscribeRequest):
    return {"url": request.url}
