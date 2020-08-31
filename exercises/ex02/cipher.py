"""This program encodes strings using a caeser cipher."""

__author__ = "730443739"

def encode_char(char: str):
    """This function encodes a single-lettered string by a shift value of 1."""
    charLower: str = char.lower()
    ascii: int = ord(charLower)
    normalized_ascii: int = ascii - 97
    encoded_ascii: int = (normalized_ascii + 1) % 26 + 97
    encoded_char: str = chr(encoded_ascii)
    print(encoded_char)

def encode_str(string: str):
    """This function encodes a 4-letter string by a shift value of 1."""
    strLower: str = string.lower()
    ascii0: int = ord(strLower[0])
    ascii1: int = ord(strLower[1])
    ascii2: int = ord(strLower[2])
    ascii3: int = ord(strLower[3])
    normalized_ascii0: int = ascii0 - 97
    normalized_ascii1: int = ascii1 - 97
    normalized_ascii2: int = ascii2 - 97
    normalized_ascii3: int = ascii3 - 97
    encoded_ascii0: int = (normalized_ascii0 + 1) % 26 + 97
    encoded_ascii1: int = (normalized_ascii1 + 1) % 26 + 97
    encoded_ascii2: int = (normalized_ascii2 + 1) % 26 + 97
    encoded_ascii3: int = (normalized_ascii3 + 1) % 26 + 97
    encoded_str: str = (chr(encoded_ascii0) + chr(encoded_ascii1) + chr(encoded_ascii2) + chr(encoded_ascii3))
    print(encoded_str)

def decode_char(char: str):
    """This function decodes a single-lettered string by a shift value of 1."""
    charLower: str = char.lower()
    ascii: int = ord(charLower)
    normalized_ascii: int = ascii - 97
    decoded_ascii: int = (normalized_ascii - 1) % 26 + 97
    decoded_char: str = chr(decoded_ascii)
    print(decoded_char)

def decode_str(string: str):
    """This function encodes a 4-letter string by a shift value of 1."""
    strLower: str = string.lower()
    ascii0: int = ord(strLower[0])
    ascii1: int = ord(strLower[1])
    ascii2: int = ord(strLower[2])
    ascii3: int = ord(strLower[3])
    normalized_ascii0: int = ascii0 - 97
    normalized_ascii1: int = ascii1 - 97
    normalized_ascii2: int = ascii2 - 97
    normalized_ascii3: int = ascii3 - 97
    decoded_ascii0: int = (normalized_ascii0 - 1) % 26 + 97
    decoded_ascii1: int = (normalized_ascii1 - 1) % 26 + 97
    decoded_ascii2: int = (normalized_ascii2 - 1) % 26 + 97
    decoded_ascii3: int = (normalized_ascii3 - 1) % 26 + 97
    decoded_str: str = (chr(decoded_ascii0) + chr(decoded_ascii1) + chr(decoded_ascii2) + chr(decoded_ascii3))
    print(decoded_str)