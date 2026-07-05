from typing import Annotated
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None


@app.get("/")
async def root():
    return {"message": "Hello"}

@app.put("/items/{item_id}") # Update
async def update_item(
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body()]
):
    results = {
        "item_id": item_id,
        "user": user,
        "item": item,
        "importance": importance
        }
    return results