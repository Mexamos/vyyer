import random

from faker import Faker
from sqlmodel import Session

from db.connection import init_db, engine
from db.models import Scans, Identities

COUNT = 200


def generate_objects():
    fake = Faker()

    objects = []
    for _ in range(COUNT):
        objects.extend([
            Scans(
                user_id=fake.md5(),
                orientation=random.choice([0, 1]),
                license_number=fake.random_int(),
                birthday=fake.date_time()
            ),
            Identities(
                vip=random.choice([0, 1]),
                ban=random.choice([0, 1]),
                start=fake.past_datetime(),
                end=fake.future_datetime()
            )
        ])
    return objects


def main():
    objects = generate_objects()
    with Session(engine) as session:
        session.add_all(objects)
        session.commit()


if __name__ == '__main__':
    init_db()
    main()
