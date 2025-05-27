from fastapi import HTTPException
from fastapi.responses import JSONResponse

def success_response(message: str, data: dict = None):
    return JSONResponse(content={
        "status": "success",
        "message": message,
        "data": data or {}
    }, status_code=200)

def error_response(message: str, status_code: int = 400):
    raise HTTPException(status_code=status_code, detail={
        "status": "error",
        "message": message,
    })