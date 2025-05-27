from db.db import Base
from .utils.default_entity import DefaultEntity
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from jwt_refresh import JwtRefresh
import uuid

class MstUsers(Base, DefaultEntity):
    
    __tablename__ = "mst_users"

    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    userinfo_id = Column(UUID(as_uuid=True), ForeignKey("mst_userinfos.id") ,default=uuid.UUID, nullable=False)
    roles_id = Column(UUID(as_uuid=True), ForeignKey("mst_roles.id") ,default=uuid.UUID, nullable=False)
    reset_token = Column(String, nullable=False)
    is_reset = Column(Boolean, default=False, nullable=False)

    userinfos = relationship("MstUserInfos", foreign_keys=[userinfo_id], back_populates="users")
    roles = relationship("MstRoles", foreign_keys=[roles_id], back_populates="users")
    jwt_refresh = relationship("JwtRefresh", foreign_keys=[JwtRefresh.user_id], back_populates="users")