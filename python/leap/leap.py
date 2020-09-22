def is_leap_year(year: int):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
