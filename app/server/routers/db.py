from fastapi import APIRouter

router = APIRouter()

@router.put("/user/{user_id}/store")
async def store(user_id: str):
    return {"welcome"}
