from typing import Annotated
from fastapi import FastAPI, Body, Query, Path
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        title="The description of the item",
        max_length=300
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than zero"
    )
    tax: float | None = None

@app.get("/")
async def root():
    return { "message": "Hello"}

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Annotated[Item, Body(embed=True)],
    q: Annotated[str | None, Path(alias="prefix-index")] = None
):
    results = {
        "item_id": item_id,
        "item": item
    }
    if q:
        results.update({"q": q})

    return results