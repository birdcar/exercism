from string import ascii_lowercase


def is_pangram(sentence: str):
    """
    Determines if a sentence is a pangram.

    A pangram (Greek: παν γράμμα, pan gramma, "every letter") is a sentence
    using every letter of the alphabet at least once.
    """
    try:
        alphabet = list(ascii_lowercase)
        letter_list = sorted(set(char for char in sentence.lower() if char.isalpha()))

        if letter_list == alphabet:
            return True

    except AttributeError:
        print(f"Pangrams must be strings, you input a {sentence}")

    return False
