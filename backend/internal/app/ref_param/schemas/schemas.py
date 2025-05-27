from pydantic import BaseModel
from utils.schemas.base import BaseEntity
from typing import Optional

class RefParamRequest(BaseModel):
    key: str
    value: str
    description: Optional[str] = None
    type: str

class RefParamResponse(BaseEntity,RefParamRequest):
    pass