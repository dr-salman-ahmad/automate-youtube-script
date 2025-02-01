from fastapi import FastAPI
from .routers import transcription

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "It is the root page"}
