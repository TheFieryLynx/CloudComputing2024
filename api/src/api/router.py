from fastapi import APIRouter, HTTPException

from src.database.database import create_user
from src.models.user import User

router = APIRouter()


@router.post("/users/")
async def add_user(email: str, first_name: str, last_name: str):
    user = User(email=email, first_name=first_name, last_name=last_name)
    user_id = create_user(user)
    if user_id:
        return {"id": user_id}
    else:
        raise HTTPException(status_code=500, detail="User not created")
