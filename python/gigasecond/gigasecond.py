import datetime as dt


def add_gigasecond(birth_date: dt.datetime):
    """
    Calculate the moment when someone has lived for 10**9 seconds.
    """
    return birth_date + dt.timedelta(seconds=10**9)
