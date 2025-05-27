from pydantic import BaseModel, EmailStr
import datetime

class UserinfoResponse(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    no_hp: str
    place_of_birth: str
    date_of_birth: datetime
    residential_address: str
    is_active = bool
    file_url = str
    religion_id = str
    gender_id = str

class RegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password: str
    roles_id: str
    userinfo_id: str

class RegisterResponse(BaseModel):
    email: EmailStr
    username: str
    password: str
    roles_id: str
    userinfo_id: str
    userinfo_data: UserinfoResponse
