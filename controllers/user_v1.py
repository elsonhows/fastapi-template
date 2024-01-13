from typing import List
from fastapi import APIRouter

from schemas.user_schema import User

router = APIRouter()


@router.get("/users", summary="To retrieve list of available users")
async def read_users() -> List[User]:
    """Example of detailed description, it support markdown e.g. **bold**, *italic*, etc"""
    return [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"},
        {"id": 3, "name": "Peter Tan"},
    ]
