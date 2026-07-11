from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# UserBase - contain the information for the user except password
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

# UserCreate - it is the addition of password to userbase 
class UserCreate(UserBase):
    password: str

# UserOut -
class UserOut(UserBase):
    id: int
    created_at: datetime

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

class UserInDB(UserBase):
    hashed_password: str