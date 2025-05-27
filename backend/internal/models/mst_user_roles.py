from db.db import Base
from .utils.default_entity import DefaultEntity
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

class MstUserRoles(Base, DefaultEntity):
    
    __tablename__ = "mst_user_roles"

    user_id = Column(UUID(as_uuid=True), ForeignKey("mst_users.id"), nullable=False)
    roles_id = Column(UUID(as_uuid=True), ForeignKey("mst_roles.id"), nullable=False)