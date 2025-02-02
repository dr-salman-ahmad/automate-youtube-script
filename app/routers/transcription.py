from fastapi import APIRouter
from pydantic import BaseModel
from langchain_community.document_loaders import YoutubeLoader
from app.utils.transcription_utils import get_updated_transcription


router = APIRouter()


class TranscribeRequest(BaseModel):
    url: str


@router.post("/transcribe")
async def transcribe(request: TranscribeRequest):
    try:
        loader = YoutubeLoader.from_youtube_url(request.url, add_video_info=False, language=["en", "hi"],
                                                translation="en")
        result = loader.load()
        text_content = "\n".join([doc.page_content for doc in result])
        updated_text_content = get_updated_transcription(text_content)
        return {"text": updated_text_content}
    except Exception as e:
        return {"error": str(e)}
