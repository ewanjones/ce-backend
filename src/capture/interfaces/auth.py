from capture.services.auth import InvalidUser, authenticate_user, create_access_token
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

auth_router = APIRouter(prefix="/auth")


class LoginData(BaseModel):
    username: str
    password: str


@auth_router.post("/token")
async def get_token(data: LoginData):
    try:
        user = authenticate_user(data.username, data.password)
    except InvalidUser:
        # Do not differentiate between errors for security
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
