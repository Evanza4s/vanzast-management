from db.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from .utils.default_entity import DefaultEntity
from internal.models.mst_users import MstUsers
import uuid

class MstUserInfos(Base, DefaultEntity):
    __nametable__ = "mst_userinfos"

    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    no_hp = Column(String, nullable=False)
    place_of_birth = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    residential_address = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    file_url = Column(String, nullable=True)
    religion_id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    gender_id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)

    users = relationship("MstUsers", foreign_keys=[MstUsers.userinfo_id], back_populates="user_infos")

    gender = relationship('RefParameter', foreign_keys=[gender_id])
    religion = relationship('RefParameter', foreign_keys=[religion_id])