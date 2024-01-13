from fastapi import APIRouter

router = APIRouter()


@router.get("/users", summary="To retrieve list of available users")
async def read_users():
    """Example of detailed description, it support markdown e.g. **bold**, *italic*, etc"""
    return [{"username": "John Doe"}, {"username": "Jane Doe"}]
