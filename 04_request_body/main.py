from fastapi import FastAPI
from pydantic import BaseModel

"""
When we need to send data from a client to your API, 
your send it as a request body.

1. A request body is data sent by the client to your API. A Response
body is the data your API sends to the client.
"""

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello"
    }

@app.post("/items/") # Create
async def create_items(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({
            "price_with_task": price_with_tax
        })
    return item_dict

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {
#         "item_id": item_id,
#         **item.model_dump()
#     }

@app.put("/items/{item_id}") # update
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {
        "item_id": item_id,
        **item.model_dump()
    }
    if q:
        result.update({"q": q})
    return result