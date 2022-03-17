from enum import Enum

from fastapi import APIRouter, Depends, Query
from fastapi_pagination import Page, paginate
from sqlalchemy import select
from sqlmodel import Session

from db.connection import get_session
from db.models import Identities
from views.validations import OrderDirection, IdentitiesOrder

router = APIRouter()


@router.get("/identities/get", tags=["Identity"], response_model=Page[Identities])
def get_scans(
    order: IdentitiesOrder = None,
    order_direction: OrderDirection = None,
    session: Session = Depends(get_session)
):
    query = select(Identities)
    if order is not None:
        field = getattr(Identities, order)
        if order_direction == OrderDirection.desc:
            field = field.desc()
        query = query.order_by(field)

    result = session.execute(query)
    identities = result.scalars().all()
    return paginate(identities)


@router.get("/identities/{scan_id}", tags=["Identity"])
def get_scans_by_id(identity_id: str, session: Session = Depends(get_session)):
    result = session.execute(select(Identities).where(Identities.id == identity_id))
    identity = result.scalars().first()
    return identity


@router.get("/identities/range", tags=["Identity"], response_model=Page[Identities])
def read_user(
    offset: int = 0, limit: int = Query(default=100, lte=100),
    order: IdentitiesOrder = None,
    order_direction: OrderDirection = None,
    session: Session = Depends(get_session)
):
    query = select(Identities)
    if order is not None:
        field = getattr(Identities, order)
        if order_direction == OrderDirection.desc:
            field = field.desc()
        query = query.order_by(field)

    result = session.execute(query.offset(offset).limit(limit))
    identities = result.scalars().all()
    return paginate(identities)
