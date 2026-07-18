from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def catch_all_errors(request: Request, exc: Exception):
    return JSONResponse(status_code=500,
                        content={"error": "Something went wrong!"})

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/broken")
async def broken():
    raise Exception("Oops! I Broke!")