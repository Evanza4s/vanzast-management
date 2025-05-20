from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from db.db import Base
from .utils.DefaultEntity import DefaultEntity

class MstUserRoles(Base, DefaultEntity):
    __tablename__ = "mstuser_roles"

    user_id = Column(UUID(as_uuid=True), ForeignKey("mstusers.id"), nullable=False)
    roles_id = Column(UUID(as_uuid=True), ForeignKey("mstroles.id"), nullable=False)
    is_active = Column(Boolean, nullable=False)