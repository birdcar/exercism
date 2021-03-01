import calendar as cal
import datetime as dt
from typing import Literal

VALID_DAY = Literal[
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]
VALID_WEEK = Literal["1st", "2nd", "3rd", "4th", "5th", "last", "teenth"]
DAYS = {day: n for n, day in enumerate(cal.day_name)}
WEEKS = {
    "1st": 0,
    "2nd": 1,
    "3rd": 2,
    "4th": 3,
    "5th": 4,
    "last": -1,
}


class MeetupDayException(Exception):
    """
    A Custom exception to indicate when a specified day is invalid for a given month
    """

    pass


def meetup(year: int, month: int, week: VALID_WEEK, day_of_week: VALID_DAY) -> dt.date:
    """
    Calculates the date of meetups.

    >>> meetup(2013, 5, "teenth", "Monday")
    datetime.date(2013, 5, 13)

    >>> meetup(2013, 4, "1st", "Monday")
    datetime.date(2013, 4, 1)
    """
    first_day, total_days = cal.monthrange(year, month)
    month_days_gen = (i % 7 for i in range(first_day, total_days + first_day))
    num_days_in_month = [
        date + 1
        for date, day in zip(range(total_days), month_days_gen)
        if day == DAYS[day_of_week]
    ]

    if week != "teenth" and len(num_days_in_month) < WEEKS[week] + 1:
        raise MeetupDayException("Not a valid day in the provided month and year")

    if week == "teenth":
        day = (set(range(13, 20)) & set(num_days_in_month)).pop()
    else:
        day = num_days_in_month[WEEKS[week]]

    return dt.date(year, month, day)


if __name__ == "__main__":
    meetup(2012, 12, "1st", "Friday")
