from fastapi import APIRouter
from drug_store.src.server.database.models import Application
from drug_store.src.server.database.db_manager import SessionLocal

applications_router = APIRouter()

@applications_router.post("/add_application")
async def add_application(application: Application):
    # Your logic to add an application
    db = SessionLocal()
    db.add(application)
    db.commit()
    db.refresh(application)
    db.close()
    return {"message": "Application added successfully"}
