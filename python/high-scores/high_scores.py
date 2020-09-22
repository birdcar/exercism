from typing import List


def latest(scores: List[int]) -> int:
    """
    Returns the latest score from a list of chronologically-ordered scores.
    """
    return scores[-1]


def personal_best(scores: List[int]) -> int:
    """
    Returns the highest score from a list of scores.
    """
    return max(scores)


def personal_top_three(scores: List[int]) -> List[int]:
    """
    Returns the top three scores from a list of scores in descending order.

    If there are less than three scores available, it will return whatever
    values are available in descending order.
    """
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores if len(scores) <= 3 else sorted_scores[:3]

