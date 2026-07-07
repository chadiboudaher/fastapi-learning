from typing import Annotated, Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz", 
        "description": None, 
        "price": 50.2, 
        "tax": 10.5, 
        "tags": []
    },
}

@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/items/{item_id}", response_model=Item, response_model_include={"name", "description"})
async def read_item(item_id: str):
    return items[item_id]

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]