from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# ---- USer Models ----
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    """ Used when creating a new user """
    password: str

class UserOut(UserBase):
    """ What the user receives """
    id: int
    created_at: datetime

class UserUpdate(BaseModel):
    """ Used when updating a user """    
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

class UserInDB(UserBase):
    """ Internal user model """
    id: int
    hashed_password: str
    disabled: bool = False
    created_at: datetime


# ---- Notes models ----

class NoteBase(BaseModel):
    title: str
    content: str
    is_public: bool = False

