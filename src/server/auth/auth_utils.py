from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Placeholder logic: Validate token and fetch user
    # For now, let's assume we return a dummy user
    user = {"username": "john_doe", "role": "admin"}
    return user
