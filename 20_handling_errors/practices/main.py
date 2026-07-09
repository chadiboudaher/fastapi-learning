from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

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
    id = max(users_db.keys()) + 1
    users_db[id] = user.dict()
    return {
        "id": id,
        **user.dict()
    }