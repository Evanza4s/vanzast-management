from sqlalchemy import Column, ForeignKey, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .utils.DefaultEntity import DefaultEntity
from db.db import Base
import uuid

class MstUsers(Base, DefaultEntity):
    __tablename__ = "mst_users"

    email = Column(String,unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    userinfo_id = Column(UUID(as_uuid=True), ForeignKey("mst_user_info.id"), default=lambda: str(uuid.uuid4()), index=True,  nullable=False)
    roles_id = Column(UUID(as_uuid=True), ForeignKey("mst_roles.id") ,default=lambda: str(uuid.uuid4()), index=True)
    reset_token = Column(String, nullable=True)
    isDeleted = Column(Boolean, default=False, nullable=False)

    roles = relationship("MstRoles", foreign_keys=[roles_id], back_populates="users")
    user_infos = relationship("MstUserInfos", foreign_keys=[userinfo_id], back_populates="users")