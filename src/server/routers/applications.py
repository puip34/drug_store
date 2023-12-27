from fastapi import APIRouter, Depends
from drug_store.src.server.auth.auth_utils import get_current_user

router = APIRouter(prefix='/applications', tags=["Applications"])

@router.post("/add", response_model=dict)
async def add_application(
    drug: str,
    customer: str,
    current_user: dict = Depends(get_current_user)
):
    
    return {"message": "Application added successfully"}
