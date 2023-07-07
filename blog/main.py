from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException, Request, Response, status, Depends
from . import schemas, models, db

app = FastAPI()
templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(db.engine)


@app.get("/", response_class=HTMLResponse)
async def create_blog(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})
