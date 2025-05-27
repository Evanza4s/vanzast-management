from fastapi import APIRouter
from internal.app.ref_param.handler import router as ref_handler

router = APIRouter()

@router.get("/")
async def root_api():
    return {"Get Start"}

router.include_router(ref_handler, prefix="/ref-param", tags=["Ref Parameter"])