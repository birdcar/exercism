from string import ascii_lowercase as lwr
from string import ascii_uppercase as upr


def rotate(text: str, key: int) -> str:
    translation = str.maketrans(
        lwr + upr, (lwr[key:] + lwr[:key]) + (upr[key:] + upr[:key])
    )
    return text.translate(translation)
