from sqlalchemy import Column, String, Text
from db.db import Base
from .utils.DefaultEntity import DefaultEntity
from sqlalchemy.dialects.postgresql import UUID

class RefParameter(Base, DefaultEntity):
    __tablename__ = "ref_parameter"

    key = Column(String, nullable=True)
    value = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    type = Column(String, nullable=True)