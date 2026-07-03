from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# 1. Pass a path and return the id in a message
# 2. Identify the type of parameter set

# @app.get("/users/me")
# async def read_user_me():
#     return {
#         "user_id": "The current user"
#     }

# @app.get("/users/{user_id}")
# async def read_user(user_id: int):
#     return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {
            "model_name": model_name,
            "message": "Deep Learning FTW!",
        }
    
    if model_name.value == "lenet":
        return {
            "model_name": model_name,
            "message": "LeCNN all the images"
        }
    
    return {
        "model_name": model_name,
        "message": "Have some residual"
    }


# Path inside a path
# /files/{file_path:path}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}