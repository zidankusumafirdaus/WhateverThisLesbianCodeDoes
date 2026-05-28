from datetime import date, datetime
from decimal import Decimal


def to_number(value):
    if isinstance(value, Decimal):
        return float(value)
    return value


def to_date(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return value
