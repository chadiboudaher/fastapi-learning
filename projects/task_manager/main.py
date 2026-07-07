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
    x_user_id: Annotated[int, Header(..., description="User id for auth")]
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

@app.get("/tasks/")
async def get_tasks(
    x_user_id: Annotated[int, Header(..., description="User ID for authentication")],
    skip: int = Query(0, ge=0, description="Number of tasks to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max tasks to return"),
    status: Optional[Status] = Query(None, description="Filter by status")
):
    tasks = db.get_all(x_user_id, skip, limit, status)
    return tasks

@app.get("/tasks/{task_id}")
async def get_task(
    task_id: int,
    x_user_id: Annotated[int, Header(..., description="User ID for authentication")]
):
    task = db.get_one(task_id, x_user_id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"Task with ID {task_id} not found"
        )
    return task

@app.put("/tasks/{task_id}")
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    x_user_id: Annotated[int, Header(..., description="User ID for authentication")]
):
    update_task = db.update(task_id, x_user_id, task_update)
    if not update_task:
        raise HTTPException(
            status_code=404,
            detail=f"Task with ID {task_id} not found"
        )
    return update_task