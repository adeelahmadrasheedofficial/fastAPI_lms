from typing import Optional, List

import fastapi
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None




@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Successfully created"


@router.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., description="ID to retrieve the user", gt=0),
                   q : str = Query(None, max_length=10)):
    return {"user": users[user_id], "query": q}
