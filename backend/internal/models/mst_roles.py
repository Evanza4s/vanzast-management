from db.db import Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from .utils.default_entity import DefaultEntity
from internal.models.mst_users import MstUsers

class MstRoles(Base, DefaultEntity):
    
    __tablename__ = "mst_roles"

    role_name = Column(String, unique=True, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    is_super_admin = Column(Boolean, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)

    users = relationship("MstUsers", foreign_keys=[MstUsers.roles_id], back_populates="roles")
