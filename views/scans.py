from enum import Enum

from fastapi import APIRouter, Depends, Query
from fastapi_pagination import Page, paginate
from sqlalchemy import select
from sqlmodel import Session

from db.connection import get_session
from db.models import Scans
from views.validations import OrderDirection, ScansOrder

router = APIRouter()


@router.get("/scans/get", tags=["Scan"], response_model=Page[Scans])
def get_scans(
    order: ScansOrder = None,
    order_direction: OrderDirection = None,
    session: Session = Depends(get_session)
):
    query = select(Scans)
    if order is not None:
        field = getattr(Scans, order)
        if order_direction == OrderDirection.desc:
            field = field.desc()
        query = query.order_by(field)

    result = session.execute(query)
    scans = result.scalars().all()
    return paginate(scans)


@router.get("/scans/range", tags=["Scan"], response_model=Page[Scans])
def get_scans_range(
    offset: int = 0, limit: int = Query(default=100, lte=100),
    order: ScansOrder = None,
    order_direction: OrderDirection = None,
    session: Session = Depends(get_session)
):
    query = select(Scans)
    if order is not None:
        field = getattr(Scans, order)
        if order_direction == OrderDirection.desc:
            field = field.desc()
        query = query.order_by(field)

    result = session.execute(query.offset(offset).limit(limit))
    scans = result.scalars().all()
    return paginate(scans)


@router.get("/scans/{scan_id}", tags=["Scan"])
def get_scan_by_id(scan_id: str, session: Session = Depends(get_session)):
    result = session.execute(select(Scans).where(Scans.id == scan_id))
    scan = result.scalars().first()
    return scan
