from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import get_db
from internal.app.ref_param.schemas.schemas import RefParamRequest, RefParamResponse
from internal.app.ref_param.service import RefService
from utils.response.response import error_response, success_response

router = APIRouter()

@router.post("/add", response_model=RefParamResponse)
def save_ref_param(
    data: RefParamRequest,
    db: Session = Depends(get_db)
):
    try:
        ref = RefService.create_ref(db, data)
        if ref is None:
            return error_response(
                status_code=400,
                message="Failed to create parameter"
            )
        return success_response(
            message="Parameter created successfully",
            data=RefParamResponse.from_orm(ref).dict()
        )
    except Exception as e:
        return error_response(
            status_code=400,
            message=str(e)
        )
    
@router.put("/update/{item_id}", response_model=RefParamResponse)
async def update_ref(
    item_id: str,
    data: RefParamRequest,
    db: Session = Depends(get_db)
):
    try:
        ref = RefService.update_ref(db, item_id, data)
        return success_response(
            message="Reference updated successfully",
            data=RefParamRequest.from_orm(ref).dict
        )
    except Exception as e:
        return error_response(
            status_code=400,
            message=str(e)
        )
    
@router.delete("/delete/{item_id}", response_model=RefParamResponse)
async def delete_ref(
    item_id: str,
    db: Session = Depends(get_db)
):
    try:
        ref = RefService.delete_ref(db, item_id)
        return success_response(
            message="Reference deleted successfully",
            data=RefParamRequest.from_orm(ref).dict
        )
    except Exception as e:
        return error_response(
            status_code=400,
            message=str(e)
        )