from fastapi import FastAPI, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session


app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello world"}
