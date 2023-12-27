import fastapi
from drug_store.src.server.database.models import Users
from drug_store.src.server.resolvers import users

users_router = fastapi.APIRouter(prefix='/users', tags=["Users"])

@users_router.post(path='/login', response_model=dict)
def login(username: str, password: str) -> dict:
    return users.login(username, password)

@users_router.put(path='/change_password/{user_id}', response_model=dict)
def change_password(user_id: int, new_password: str) -> dict:
    return users.change_password(user_id, new_password)
