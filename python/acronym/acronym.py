def parse_words(words: str) -> str:
    """
    Returns the string `words` after removing punctuation and title-casing
    each word.
    """
    return words.translate(
        str.maketrans("-", " ", "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~")
    ).title()


def abbreviate(words: str) -> str:
    """
    Returns a naieve abbreviation made up of the first letter of each word in
    the string `words`
    """
    return "".join(char for char in parse_words(words) if char.isupper())
