from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
# from starlette.exceptions import HTTPException as ScarletteHTTPException
from pydantic import BaseModel

"""
HTTPException - For raising HTTP errors in your routes
RequestValidationError - FastAPI's exception for invalid request data
PlainTextResponse - Returns raw text instead of JSON
ScarletteHTTPException - Starlette's base HTTP exception (parent of FastAPI's)
"""

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({
            "detail": exc.errors(),
            "body": exc.body
        })
    )

class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item
    

# @app.exception_handler(ScarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), 
#                              status_code=exc.status_code)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request,
#                                        exc: RequestValidationError):
#     message = "Validation Erros:"
#     for error in exc.errors():
#         message += f"\nField: {error['loc']}, Error: {error['msg']}"
#     return PlainTextResponse(message, status_code=400)

# @app.get("/items/{item_id}")
# async def read(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418,
#                             detail="Nope! I don't like 3.")
#     return {"item_id": item_id}