from datetime import datetime


def is_valid_date(value):

    if not isinstance(value, str):
        return False

    if len(value) != 10:
        return False

    if value[4] != "-" or value[7] != "-":
        return False

    if not all(
        char.isdigit()
        for index, char in enumerate(value)
        if index not in (4, 7)
    ):
        return False

    try:
        datetime.strptime(
            value,
            "%Y-%m-%d",
        )
        return True

    except ValueError:
        return False