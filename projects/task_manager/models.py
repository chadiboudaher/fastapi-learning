from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Status(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Priority = Priority.MEDIUM
    status: Status = Status.PENDING

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[Priority] = None
    status: Optional[Status] = None

class TaskResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]
    priority: Priority
    status: Status
    created_at: datetime
    updated_at: datetime