from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root_api():
    return {"Get Start"}
