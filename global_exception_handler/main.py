from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from datetime import datetime

app = FastAPI()

@app.exception_handler(Exception)
async def catch_all_errors(request: Request, exc: Exception):
    return JSONResponse(status_code=500,
                        content={
                            "success": False,
                            "timestamp": datetime.now().isoformat(),
                            "path": request.url.path,
                            "error": {
                                "message": str(exc),
                                "type": type(exc).__name__
                            }
                        })

# User send wrong data
@app.exception_handler(RequestValidationError)
async def handle_validation_error(request, exc):
    return JSONResponse(
        status_code=422,
        content={"content": "Your data is invalid!",
                 "detail": str(exc)}
    )

# User asks for something that does not exist
@app.exception_handler(404)
async def handle_not_found(request, exc):
    return JSONResponse(
        status_code=404,
        content={"error": "This doesn't exist"}
    )

# Database is down
# @app.exception_handler(Exception)
# async def handle(request, exc):
#     return JSONResponse(
#         status_code=500,
#         content={"error": "Our servers are having issues!"}
#     )

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/broken")
async def broken():
    raise Exception("Oops! I Broke!")