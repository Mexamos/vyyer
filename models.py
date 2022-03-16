from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, JSON
from sqlalchemy.dialects.mysql import INTEGER

Base = declarative_base()
metadata = Base.metadata


class Scans(Base):
    __tablename__ = 'scans'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(String(255))
    orientation = Column(INTEGER(1))
    license_number= Column(String(255))
    birthday = Column(TIMESTAMP)


class Identities(Base):
    __tablename__ = 'identities'

    id = Column(INTEGER(11), primary_key=True)
    user_ids = Column(JSON)
    ban = Column(INTEGER(1))
    start= Column(TIMESTAMP)
    end = Column(TIMESTAMP)
