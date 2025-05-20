from sqlalchemy import Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from internal.models.utils.DefaultEntity import DefaultEntity
from internal.models.MstUsers import MstUsers
from db.db import Base

class MstRoles(Base, DefaultEntity):
    __nametable__ = "mst_roles"

    role_name = Column(String, unique=True, nullable=False)
    is_admin = Column(Boolean, nullable=True)
    is_super_admin = Column(Boolean, nullable=True)
    is_deleted = Column(Boolean, default=False, nullable=True)

    users = relationship("MstUsers", foreign_keys=[MstUsers.roles_id], back_populates="mst_roles")