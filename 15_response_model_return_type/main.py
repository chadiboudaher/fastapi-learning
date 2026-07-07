from typing import Annotated, Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Item:
    return item

@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0)
    ]

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user