from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_handler(requst: Request,
                             exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = error["loc"][-1]
        msg = error["msg"]
        errors.append(f"{field}: {msg}")

    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation Field",
            "details": errors
        }
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request,
                                 exc: HTTPException):
    return JSONResponse(status_code=exc.status_code,
                        content={
                            "error": exc.detail,
                            "status": exc.status_code
                        })

class User(BaseModel):
    name: str
    age: int

users_db = {
    1: {
        "name": "chadi",
        "age": 20
    },
    2: {
        "name": "Sunoo",
        "age": 25
    }
}

@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """
    raise HTTPException if not found
    """
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {user_id} not found")
    return users_db[user_id]

@app.post("/users/")
async def create_user(user: User):

    for existing in users_db.values():
        if existing["name"] == user.name:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"User {user.name} already exists")

    if user.age  < 0 or user.age > 120:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Age must bebetween 0 and 120")
    id = max(users_db.keys()) + 1
    users_db[id] = user.dict()
    return {
        "id": id,
        **user.dict()
    }