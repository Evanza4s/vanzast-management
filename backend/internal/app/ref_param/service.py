from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from internal.models.ref_parameter import RefParameter
from internal.app.ref_param.schemas.schemas import RefParamRequest, RefParamResponse
from utils.response.response import error_response

class RefService:

    @staticmethod
    def create_ref(db: Session, item: RefParamRequest) -> RefParameter:
        try:
            now = datetime.now()
            new_data = RefParameter(**item.dict(), created_at=now, is_deleted=True)

            db.add(new_data)
            db.commit()
            db.refresh(new_data)

            return new_data
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def update_ref(db: Session, item_id: str, item: RefParamRequest) -> RefParameter:
        db_item = db.query(RefParameter).filter((RefParameter.id == item_id) & (RefParameter.is_deleted == False)).first()

        if not db_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Data Not Found or Already Deleted"
            )
        
        now = datetime.now()

        for key, value in item.dict(exclude_unset=True).items():
            setattr(db_item, key, value)

        db_item.updated_at = now

        db.commit()
        db.refresh(db_item)

        return db_item
    
    @staticmethod
    def delete_ref(db: Session, item_id: str) -> RefParameter:
        db_item = db.query(RefParameter).filter((RefParameter.id == item_id) | (RefParameter.is_deleted == False)).first()

        if not db_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Data Not Found or Already Deleted"
            )
        
        now = datetime.now()

        db_item.deleted_at = now
        db_item.is_deleted = True

        db.commit()
        db.refresh(db_item)

        return db_item
