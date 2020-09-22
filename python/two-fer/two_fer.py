def two_fer(name: str = "you") -> str:
    """
    Returns the string "One for X, one for me.", interpolating "you" when
    the `name` parameter is not provided, and `name` otherwise.

    >>> two_fer()
    "One for you, one for me."

    >>> two_fer("Alice")
    "One for Alice, one for me."
    """
    return f"One for {name}, one for me."
