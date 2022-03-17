from db.settings import DB_URL

from sqlmodel import create_engine, SQLModel, Session

engine = create_engine(DB_URL)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
