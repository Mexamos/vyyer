from fastapi import APIRouter

router = APIRouter()


@router.get("/scans/get", tags=["Scan"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/scans/{id}", tags=["Scan"])
async def read_user_me(identity_id: str):
    return {"username": identity_id}


@router.get("/scans/range", tags=["Scan"])
async def read_user():
    return {"username": 'hello'}