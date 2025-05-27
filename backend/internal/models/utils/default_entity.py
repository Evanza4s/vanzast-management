from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_mixin
import uuid

@declarative_mixin
class DefaultEntity:
    id = Column(UUID(as_uuid=True),
                primary_key=True,
                default=uuid.uuid4,
                index=True,
    )
    created_by = Column(
        UUID(as_uuid=True), 
        ForeignKey("mst_users.id"), 
        nullable=True, 
        doc="ID of the user who created the record."
    )
    updated_by = Column(
        UUID(as_uuid=True), 
        ForeignKey("mst_users.id"), 
        nullable=True, 
        doc="ID of the user who last updated the record."
    )
    deleted_by = Column(
        UUID(as_uuid=True), 
        ForeignKey("mst_users.id"), 
        nullable=True, 
        doc="ID of the user who deleted the record."
    )
    created_at = Column(
        DateTime(timezone=True), 
        default=func.now(), 
        nullable=False, 
        doc="Timestamp when the record was created."
    )
    updated_at = Column(
        DateTime(timezone=True), 
        onupdate=func.now(), 
        nullable=True, 
        doc="Timestamp when the record was last updated."
    )
    deleted_at = Column(
        DateTime(timezone=True), 
        nullable=True, 
        doc="Timestamp when the record was deleted."
    )
