from fastapi import FastAPI
from fastapi_pagination import add_pagination

from views import scans, identities
from db.connection import init_db

app = FastAPI()

app.include_router(scans.router)
app.include_router(identities.router)

add_pagination(app)


@app.on_event("startup")
def on_startup():
    init_db()
