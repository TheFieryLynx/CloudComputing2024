from fastapi import APIRouter, HTTPException

from src.database.database import create_user, get_user_by_id
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


@router.get("/users/{user_id}")
async def add_user(user_id: int):
    data = get_user_by_id(user_id)
    print(data)

    if len(data) > 0:
        return User(user_dict=data[0])
    else:
        raise HTTPException(status_code=500, detail="User not found")
