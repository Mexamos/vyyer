from fastapi import APIRouter

router = APIRouter()


@router.get("/identities/get", tags=["Identity"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/identities/{id}", tags=["Identity"])
async def read_user_me(identity_id: str):
    return {"username": identity_id}


@router.get("/identities/range", tags=["Identity"])
async def read_user():
    return {"username": 'hello'}