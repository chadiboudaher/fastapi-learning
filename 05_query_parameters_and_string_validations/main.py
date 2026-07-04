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
    hidden_query: Annotated[str | None, Query(
        include_in_schema=False
        )] = None):
    # results = {"items": [
    #     {"item_id": "Foo"},
    #     {"item_id": "Bar"}
    # ]}
    if hidden_query:
        return {"hidden_query": hidden_query}
    
    else:
        return {"hidden_query": "Not Found"}