from fastapi import FastAPI, HTTPException, Response, status, Depends
from blog.schemas import Blog
from . import schemas, models, db

# from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(db.engine)


@app.post("/blogs/")
async def create_blog(blog: Blog):
    return blog
