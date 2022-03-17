from enum import Enum


class OrderDirection(str, Enum):
    asc = "asc"
    desc = "desc"


class ScansOrder(str, Enum):
    id = "id"
    user_id = "user_id"
    orientation = "orientation"
    license_number = "license_number"
    birthday = "birthday"


class IdentitiesOrder(str, Enum):
    id = "id"
    vip = "vip"
    ban = "ban"
    start = "start"
    end = "end"
