from fastapi import APIRouter, Depends
from drug_store.src.server.auth.auth_utils import get_current_user

router = APIRouter(prefix='/users', tags=["Users"])

@router.get("/me", response_model=dict)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
