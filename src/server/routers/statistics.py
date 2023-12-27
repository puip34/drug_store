from fastapi import APIRouter, Depends
from drug_store.src.server.auth.auth_utils import get_current_user

router = APIRouter(prefix='/statistics', tags=["Statistics"])

@router.get("/performance", response_model=dict)
async def get_performance_statistics(
    current_user: dict = Depends(get_current_user)
):
    # Placeholder logic: Here you can fetch performance statistics from the database
    return {"message": "Performance statistics retrieved successfully"}
