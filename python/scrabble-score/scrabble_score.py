from typing import Dict

# Generates a mapping of letters to their scrabble score e.g. 
#
#     { 'A': 1, ..., 'Z': 10 }
#
SCORE_SHEET: Dict[str, int] = dict(
    [(x, 1) for x in 'AEIOULNRST'] +
    [(x, 2) for x in 'DG'] +
    [(x, 3) for x in 'BCMP'] +
    [(x, 4) for x in 'FHVWY'] +
    [(x, 5) for x in 'K'] +
    [(x, 8) for x in 'JX'] + 
    [(x, 10) for x in 'QZ']
)


def score(word: str) -> int:
    """
    Given a word, compute the scrabble score for that word.
    """
    if not x.isalpha():
        return 0
    return sum(SCORE_SHEET[char] for char in word.upper())

