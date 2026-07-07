from fastapi import FastAPI, HTTPException, Header, Query
from typing import Optional, List, Annotated
from models import TaskCreate, TaskUpdate, TaskResponse, Priority, Status
from database import db

app = FastAPI(
    title="Task Manager",
    description="Simple Task Management System",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Hello"}

# --- Task Operations ---

@app.post("/tasks/", response_model=TaskResponse, status_code=201)
async def create_task(
    task: TaskUpdate,
    x_user_id: Annotated[int, Header(description="User id for auth")]
):
    """
    Create a new task for authenticated user

    - title (required)
    - description (Optional)
    - priority: low, medium, high (default: medium)
    - status: pending, in_progress, completed (default: pending)
    """

    new_task = db.create(x_user_id, task)
    return new_task