from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BaseEntity(BaseModel):
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[str] = None
    is_deleted: Optional[bool] = None

    class Config:
        from_attributes = True