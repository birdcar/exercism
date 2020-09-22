"""Python solution to the Word Count exercise from Exercism.io."""
import re
from collections import Counter


def word_count(phrase):
    """Given a phrase, count the occurrences of each word in that phrase."""
    return Counter(
        re.findall(r"\w+(?:'\w+)?", phrase.replace('_', ' ').lower()))