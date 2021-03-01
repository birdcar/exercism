def is_armstrong_number(number: int) -> bool:
    """
    Given a number, determine if it is an Armstrong number.

    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

    >>> is_armstrong_number(10)
    False

    >> is_armstrong_number(153)
    True
    """
    num_str = str(number)

    return number == sum(
        map(lambda digit: digit ** len(num_str), [int(num) for num in num_str])
    )
