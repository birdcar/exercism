import re


REPEATS_RE = re.compile(r"(.)\1*")
NUMBERS_RE = re.compile(r"(\d+)(.)")


def to_numbers(match: re.Match):
    """
    A re.match 'repl' Callable used to generate a Run Length Encoded string
    """
    length = len(match.group(0))
    return str(length) + match.group(1) if length > 1 else match.group(1)


def from_numbers(match: re.Match):
    """
    A re.match `repl` Callable used to interpret a Run Lengh Encoded string
    """
    return int(match.group(1)) * match.group(2)


def encode(string: str):
    """
    Compress a string using Run Length Encoding.
    """
    return REPEATS_RE.sub(to_numbers, string)


def decode(string: str):
    """
    Decompress a Run Length Encoded string and return the original.
    """
    return NUMBERS_RE.sub(from_numbers, string)
