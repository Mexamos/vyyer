from datetime import datetime

from sqlmodel import SQLModel, Field


class Scans(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: str
    orientation: int
    license_number: int
    birthday: datetime


class Identities(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    vip: int
    ban: int
    start: datetime
    end: datetime
