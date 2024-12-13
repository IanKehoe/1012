from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.routes import items, auth
from app.core.database import get_db, engine

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

app.include_router(items.router)
app.include_router(auth.router, prefix="/auth")