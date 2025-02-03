import os
import uuid
from fastapi import APIRouter
from dotenv import load_dotenv
from pydantic import BaseModel
from elevenlabs.client import ElevenLabs


load_dotenv()
router = APIRouter()


client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))


class GenerateAudioRequest(BaseModel):
    transcription: str


@router.post("/generate-audio")
async def generate_audio(request: GenerateAudioRequest):
    try:
        audio = client.text_to_speech.convert(
            text=request.transcription,
            voice_id="NFG5qt843uXKj4pFvR7C",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        # Generate a unique filename using UUID
        unique_filename = f"audio_{uuid.uuid4().hex}.mp3"
        output_path = os.path.join("audio_files", unique_filename)

        # Ensure the directory exists
        os.makedirs("audio_files", exist_ok=True)

        # Save the audio file asynchronously
        with open(output_path, "wb") as file:
            for chunk in audio:  # Iterate over the generator
                file.write(chunk)  # Write each chunk to the file

        return {"message": "Audio generated successfully", "file_path": output_path, "status": "success"}
    except Exception as e:
        return {"message": "Failed to generate audio", "error": str(e), "status": "error"}
