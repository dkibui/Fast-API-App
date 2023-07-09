from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException, Request, Response, status, Depends, Header

from .db import conn, cursor

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def create_blog(
    request: Request,
    hx_request: Optional[str] = Header(None),
    page: int = 1,
):
    N = 3
    OFFSET = (page - 1) * N
    cursor.execute(
        """SELECT * FROM public.films ORDER BY id ASC OFFSET %s LIMIT %s""",
        (
            OFFSET,
            N,
        ),
    )
    films = cursor.fetchall()
    # cursor.close()
    # conn.close()
    context = {
        "request": request,
        "films": films,
        "page": page,
    }
    if hx_request:
        return templates.TemplateResponse("table.html", context)
    return templates.TemplateResponse("index.html", context)
