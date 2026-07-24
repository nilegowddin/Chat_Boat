from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.controllers.chat_controller import router as chat_router
from app.controllers.upload_controller import router as upload_router

app = FastAPI(title="DocChat")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


app.include_router(chat_router)
app.include_router(upload_router)