from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db.db import Base
from .utils.default_entity import DefaultEntity

class JwtRefresh(Base, DefaultEntity):
    __tablename__ = "jwt_refresh"

    jwt_refresh = Column(Text, nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("mst_users.id"), nullable=False)

    users = relationship("MstUsers", foreign_keys=[user_id], back_populates="jwt_refresh")
