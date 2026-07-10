from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/")
async def root():
    return {"message": "hello"}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}")
async def update_item(item_id: str,
                      item: Item) -> Item:
    stored_item_data = items[item_id]

    # Convert stored data to pydantic model
    stored_item_model = Item(**stored_item_data)

    # Extract update data
    update_data = item.model_dump(exclude_unset=True)

    # Create updated model
    update_item = stored_item_model.model_copy(update=update_data)

    # Store updated item
    items[item_id] = jsonable_encoder(update_item)
    return update_item