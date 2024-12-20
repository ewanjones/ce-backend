from fastapi import FastAPI

from capture.data import accounts
from capture.dependencies import GetCurrentUser, Settings, db
from capture.interfaces.auth import auth_router

app = FastAPI()
settings = Settings()

models = [accounts.User]


app.include_router(auth_router)


def create_tables():
    db.create_tables(models)


@app.get("/")
async def root(username: GetCurrentUser):
    return {"message": "Hello World"}
