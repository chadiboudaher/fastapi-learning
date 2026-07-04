import random
from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

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

def chack_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get("/items/")
async def read_items(id: Annotated[str | None, AfterValidator(chack_valid_id)] = None):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.item()))
    return {"id": id, "name": item}