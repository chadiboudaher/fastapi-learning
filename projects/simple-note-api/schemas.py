from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    content: str
    is_public: Optional[bool] = False

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_public: Optional[bool] = False

class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    is_public: bool
    created_at: datetime
    updated_at: datetime
    user_id: Optional[int]

    class Config:
        from_attributes = True