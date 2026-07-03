from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# 1. Pass a path and return the id in a message
# 2. Identify the type of parameter set

@app.get("/users/me")
async def read_user_me():
    return {
        "user_id": "The current user"
    }

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}