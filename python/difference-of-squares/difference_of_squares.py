def square_of_sum(number: int, /) -> int:
    """
    Return square of the sum of the first N natural numbers, where N is the arument
    passed to `number`
    """
    return sum(range(number + 1)) ** 2


def sum_of_squares(number: int, /) -> int:
    """
    Return the sum of the squares of the first N natural numbers, where N is the
    argument passed to `number`
    """
    return sum(num ** 2 for num in range(number + 1))


def difference_of_squares(number: int, /) -> int:
    """
    Returns the difference between the square of the sum and the sum of the squares of
    the first N natural numbers, where N is the argument passed to `number`
    """
    return square_of_sum(number) - sum_of_squares(number)
