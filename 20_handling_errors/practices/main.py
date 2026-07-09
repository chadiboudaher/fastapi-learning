from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}