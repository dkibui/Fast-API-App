from fastapi import FastAPI, HTTPException, Response, status, Depends
from . import schemas, models, db

app = FastAPI()

models.Base.metadata.create_all(db.engine)


@app.post("/blogs/")
async def create_blog(blog: schemas.Blog):
    return blog
