from fastapi import FastAPI

from views import scans, identities

app = FastAPI()

app.include_router(scans.router)
app.include_router(identities.router)
