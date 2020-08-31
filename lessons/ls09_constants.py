"""Some examples of constants and functions."""

from random import choice


VOWELS: str = "aeiouy"
CONSONANTS: str = "bcdfghjklmnpqrstvwxz"

def random_letter(string: str) -> str:
    return choice(string)

print(random_letter("abc" + "def"))