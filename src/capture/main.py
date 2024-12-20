from fastapi import FastAPI
from capture.dependencies import db
from capture.data import accounts

app = FastAPI()
models = [accounts.User]


def create_tables():
    db.create_tables(models)


@app.get("/")
async def root():
    return {"message": "Hello World"}
