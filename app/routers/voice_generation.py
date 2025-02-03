import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from fastapi import APIRouter


load_dotenv()
router = APIRouter()


client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))


class GenerateAudioRequest(BaseModel):
    transcription: str


@router.post("/generate-audio")
async def generate_audio(request: GenerateAudioRequest):
    audio = client.text_to_speech.convert(
    text=request.transcription,
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)


