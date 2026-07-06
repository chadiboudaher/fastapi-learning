from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(examples=["Foo", "Boo"])
    description: str | None = Field(default=None, examples=["A very nice item", "A very shitty item"])
    price: float = Field(examples=[12.3, 12.9])
    tax: float | None = Field(default=None, examples=[3.2, 4.5])

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2
    #             }
    #         ]
    #     }
    # }

@app.get("/")
async def root():
    return {
        "message": "Hello"
    }

@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item):
    results= {"item_id": item_id, "item": item}
    return results