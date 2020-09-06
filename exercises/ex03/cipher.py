"""This program encodes strings using a caeser cipher."""


__author__ = "730443739"


def encode_char(char: str) -> str:
    """This function encodes a single-lettered string by a shift value of 1."""
    if char.islower():
        charLower: str = char.lower()
        ascii: int = ord(charLower)
        normalized_ascii: int = ascii - 97
        encoded_ascii: int = (normalized_ascii + 1) % 26 + 97
        encoded_char: str = chr(encoded_ascii)
        return encoded_char
    elif char.isupper():
        charUpper: str = char.upper()
        ascii = ord(charUpper)
        normalized_ascii = ascii - 65
        encoded_ascii = (normalized_ascii + 1) % 26 + 65
        encoded_char = chr(encoded_ascii)
        return encoded_char
    return char


def decode_char(char: str) -> str:
    """This function decodes a single-lettered string by a shift value of 1."""
    if char.islower():
        charLower: str = char.lower()
        ascii: int = ord(charLower)
        normalized_ascii: int = ascii - 97
        decoded_ascii: int = (normalized_ascii - 1) % 26 + 97
        decoded_char: str = chr(decoded_ascii)
        return decoded_char
    elif char.isupper():
        charUpper: str = char.upper()
        ascii = ord(charUpper)
        normalized_ascii = ascii - 65
        decoded_ascii = (normalized_ascii - 1) % 26 + 65
        decoded_char = chr(decoded_ascii)
        return decoded_char
    return char


def encode_str(string: str) -> str:
    """This function encodes a single-length string by a shift value of 1."""
    i: int = 0
    encoded_str: str = ""
    while i < len(string):
        char: str = string[i]
        encoded_str += encode_char(char)
        i = i + 1
    return encoded_str
    

def decode_str(string: str) -> str:
    """This function encodes a 4-letter string by a shift value of 1."""
    i: int = 0
    decoded_str: str = ""
    while i < len(string):
        char: str = string[i]
        decoded_str += decode_char(char)
        i = i + 1
    return decoded_str