from sqlalchemy import Column, ForeignKey, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from internal.models.utils.DefaultEntity import DefaultEntity
from internal.models.MstUsers import MstUsers
from db.db import Base

class MstUserInfos(Base, DefaultEntity):
    __nametable__ = "mst_userinfos"

    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    no_hp = Column(String, nullable=False)
    place_of_birth = Column(String, nullable=False)
    date_of_birth = Column(DateTime(timezone=True), nullable=False)
    residential_address = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    file_url = Column(String, nullable=True)
    gender_id = Column(UUID(as_uuid=True), ForeignKey("ref_parameter.id"), nullable=False)
    religion_id = Column(UUID(as_uuid=True), ForeignKey("ref_parameter.id"), nullable=False)


    users = relationship("MstUsers", foreign_keys=[MstUsers.userinfo_id], back_populates="mst_user_infos")

    gender = relationship('RefParameter', foreign_keys=[gender_id])
    religion = relationship('RefParameter', foreign_keys=[religion_id])