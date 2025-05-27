from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Optional
from internal.models.mst_users import MstUsers
from .jwt_auth import decode_access_token
from db.db import get_db

security = HTTPBearer()

def get_current_user(db: Session = Depends(get_db), authorization: HTTPAuthorizationCredentials = Depends(security)) -> MstUsers:
    user_data = decode_access_token(authorization.credentials)
    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    user = db.query(MstUsers).filter(MstUsers.id == user_data['user_id']).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    return user
