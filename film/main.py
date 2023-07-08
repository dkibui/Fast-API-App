from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException, Request, Response, status, Depends, Header
from psycopg2 import extras

from .db import db_connection

templates = Jinja2Templates(directory="templates")
conn = db_connection()
cursor = conn.cursor(cursor_factory=extras.DictCursor)
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def create_blog(request: Request, hx_request: Optional[str] = Header(None)):
    cursor.execute("SELECT * FROM films")
    films = cursor.fetchall()
    # cursor.close()
    # conn.close()
    context = {"request": request, "films": films}
    if hx_request:
        return templates.TemplateResponse("table.html", context)
    return templates.TemplateResponse("index.html", context)
