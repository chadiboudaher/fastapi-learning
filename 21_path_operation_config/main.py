from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

@app.post("/items/", 
          status_code=status.HTTP_201_CREATED, 
          tags=["items"],
          summary="Create an item hoe",
          description="Create a item with al the information, name, desc, price, tax")
async def create_item(item: Item) -> Item:
    return item

@app.get("/items/", tags=['items'], deprecated=True)
async def read_items():
    return [{
        "name": "Foo",
        "price": 42
    }]

@app.get("/users/", tags=['users'])
async def read_users():
    return [{
        "username": "johndoe"
    }]