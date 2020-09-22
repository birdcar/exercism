import re
from typing import List


def sum_isbn(digits: List[str]) -> bool:
    """
    Given something that appears to be an ISBN number, verify its validity
    """
    total = sum(
        [
            factors[0] * factors[1]
            for factors in zip(list(map(int, digits)), range(10, 0, -1))
        ]
    )

    return total % 11 == 0


def is_valid(isbn: str):
    """
    Given a string, verify that it's a valid ISBN number in both form
    and function
    """
    isbn = isbn.replace("-", "")
    re_valid_isbn = re.compile(r"[\d]{9}([\d]|X)$")

    if not re_valid_isbn.match(isbn):
        return False

    else:
        digits = list(isbn)

        if digits[-1] == "X":
            digits[len(digits) - 1] = "10"

        return sum_isbn(digits)

