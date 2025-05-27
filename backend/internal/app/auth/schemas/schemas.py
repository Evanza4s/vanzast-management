from pydantic import BaseModel, EmailStr
from utils.schemas.base import BaseEntity

class UserResquest(BaseModel):
    username: str
    email: EmailStr
    first_name: str = None
    last_name: str = None
    password: str
    roles_id: str

class UserSchemas(BaseModel):
    username: str
    email: EmailStr
    password: str
    roles_id: str = None
    user_info_id: str = None

    class Config:
        orm_mode = True

class UserResponse(BaseEntity, UserSchemas):
    pass