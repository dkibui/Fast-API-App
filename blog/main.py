from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException, Request, Response, status, Depends, Header
from . import schemas, models, db

from .movies import films

app = FastAPI()
templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(db.engine)


@app.get("/", response_class=HTMLResponse)
async def create_blog(request: Request, hx_request: Optional[str] = Header(None)):
    context = {"request": request, "films": films}
    if hx_request:
        return templates.TemplateResponse("table.html", context)
    return templates.TemplateResponse("index.html", context)
