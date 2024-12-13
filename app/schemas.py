from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

class AccountStatus(str, Enum):
    standard = "standard"
    admin = "admin"
    suspended = "suspended"
    banned = "banned"

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str = None
    last_name: str = None

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str = None
    last_name: str = None
    date_created: datetime
    account_status: AccountStatus
    type: int

    class Config:
        orm_mode = True