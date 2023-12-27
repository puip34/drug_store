import fastapi
from drug_store.src.server.database.models import Applications
from drug_store.src.server.resolvers import applications

applications_router = fastapi.APIRouter(prefix='/applications', tags=["Applications"])

@applications_router.post(path='/add', response_model=dict)
def add_application(application: Applications) -> dict:
    return applications.add_application(application)

@applications_router.put(path='/edit/{application_id}', response_model=dict)
def edit_application(application_id: int, new_status: str, new_drug_id: int) -> dict:
    return applications.edit_application(application_id, new_status, new_drug_id)

@applications_router.get(path='/track/{application_id}', response_model=dict)
def track_application_status(application_id: int) -> dict:
    return applications.track_application_status(application_id)

@applications_router.put(path='/assign/{application_id}', response_model=dict)
def assign_responsible(application_id: int, seller_id: int, comment: str) -> dict:
    return applications.assign_responsible(application_id, seller_id, comment)
