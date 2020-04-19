import datetime
from _exceptions import *


def is_date_valid(date: str) -> bool:
    valid = True
    yy, mm, dd = date.split('-')

    try:
        datetime.datetime(int(yy), int(dd), int(mm))
    except ValueError as e:
        valid = False

    return valid


def code_error(status_code: int) -> None:
    if status_code >= 400:
        raise RequestCodeError("Error while fetching data", coin_history.status_code)