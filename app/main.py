from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .routers import transcription, voice_generation

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(transcription.router)
app.include_router(voice_generation.router)

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
