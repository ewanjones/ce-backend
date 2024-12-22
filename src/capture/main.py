from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from capture.data import accounts, assets, ledgers
from capture.dependencies import GetCurrentUser, Settings, db
from capture.interfaces.assets import assets_router
from capture.interfaces.auth import auth_router

app = FastAPI()
settings = Settings()


app.add_middleware(
    CORSMiddleware,
    # TODO: Fix CORS
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models = [
    accounts.User,
    assets.Property,
    assets.Asset,
    assets.ChargeEvent,
    ledgers.Ledger,
    ledgers.LedgerItem,
]


app.include_router(auth_router)
app.include_router(assets_router)


def create_tables():
    db.create_tables(models)


@app.get("/")
async def root(username: GetCurrentUser):
    return {"message": "Hello World"}
