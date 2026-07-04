from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "We'll be fine"}


# @app.get("/items/")
# async def read_items(q: str | None = None):
#     results = {"items": [
#         {"item_id": "Foo"},
#         {"item_id": "Bar"}
#     ]}
#     if q:
#         results.update({"q": q})
#     return results

# we can add additional validations

@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(
        alias="item-query",
        title="Query string",
        description="Query string for the items to search the databasethat have a good match",
        min_length=3,
        max_length=50,
        pattern="^fixedquery$",
        deprecated=True
        )] = None):
    results = {"items": [
        {"item_id": "Foo"},
        {"item_id": "Bar"}
    ]}
    if q:
        results.update({"q": q})
    return results