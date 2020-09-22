from collections import Counter
from functools import partial
from typing import List, Callable

DICE_ROLL = List[int]


def number_roll(dice: DICE_ROLL, number: int) -> int:
    """
    Given a dice roll and a specific number to score against, return the score
    """
    return number * dice.count(number)


ONES = partial(number_roll, number=1)
TWOS = partial(number_roll, number=2)
THREES = partial(number_roll, number=3)
FOURS = partial(number_roll, number=4)
FIVES = partial(number_roll, number=5)
SIXES = partial(number_roll, number=6)
CHOICE = sum


def FULL_HOUSE(dice: DICE_ROLL) -> int:
    """
    Check whether a roll meets the criteria for a 'Full House'
    """
    return sum(dice) if sorted(Counter(dice).values()) == [2, 3] else 0


def FOUR_OF_A_KIND(dice: DICE_ROLL) -> int:
    """
    Check whether a roll meets the criteria for a 'Four of a Kind'
    """
    return sum([x for x in dice if dice.count(x) >= 4][:4])


def LITTLE_STRAIGHT(dice: DICE_ROLL) -> int:
    """
    Check whether a roll meets the criteria for a 'Little Straight'
    """
    return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0


def BIG_STRAIGHT(dice: DICE_ROLL) -> int:
    """
    Check whether a roll meets the criteria for a 'Big Straight'
    """
    return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0


def YACHT(dice: DICE_ROLL) -> int:
    """
    Check whether a roll meets the criteria for a 'Yacht'
    """
    return 50 if len(set(dice)) == 1 else 0


def score(dice: DICE_ROLL, category: Callable) -> int:
    """
    Given a Yacht dice roll a scoring category, return the score.
    """
    return category(dice)
