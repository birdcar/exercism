def convert(number: int) -> str:
    """
    Converts a number into a string that contains raindrop sounds corresponding
    to certain potential factors. A factor is a number that evenly divides into
    another number.

    The rules of raindrops are that if a given number:
        - has 3 as a factor, add 'Pling' to the result.
        - has 5 as a factor, add 'Plang' to the result.
        - has 7 as a factor, add 'Plong' to the result.
        - If 3, 5, or 7 are not a factor, the result should be the number.
    """
    three = "Pling" if number % 3 == 0 else ""
    five = "Plang" if number % 5 == 0 else ""
    seven = "Plong" if number % 7 == 0 else ""

    return f"{three}{five}{seven}" if three or five or seven else str(number)
