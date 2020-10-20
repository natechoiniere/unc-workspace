"""Responses for Quiz 02."""

__author__ = "730443739"

from typing import List, Dict


def capitalize(string: str) -> str:
    """Returns a string made of only the capital letters in the input string."""
    newstring: str = ""
    for i in range(len(string)):
        if string[i].isupper():
            newstring += string[i]
    return newstring


def abbreviate(string_list: List[str]) -> Dict[str, str]:
    """Returns a dictionary with a key of the full name given and a value as the abbreviated key."""  
    finished_dict: Dict[str, str] = {}
    for i in range(len(string_list)):
        finished_dict[string_list[i]] = capitalize(string_list[i])
    return finished_dict


def phonebook(int_list: List[int], string_list: List[str]) -> Dict[int, str]:
    """Returns a dictionary with a phone number as keys and values corresponding to an abbreviated name."""
    finished_dict: Dict[int, str] = {}
    if len(int_list) != len(string_list):
        raise ValueError("Parameters are not of the same length.")
    for i in range(len(int_list)):
        finished_dict[int_list[i]] = capitalize(string_list[i])
    return finished_dict


def find_ppl_in_area(dict: Dict[int, str], areacode: int) -> List[str]:
    """Returns a dictionary of phoe numbers and corresponding names whose phone numbers match the same area code."""
    finished_list: List[str] = []
    areacounter: str = ""
    k: int = 0
    if len(str(areacode)) < 3:
        raise ValueError("Area code must be exactly 3 digits.")
    for i in dict:
        for j in str(i):
            while k < 3:
                if str(i)[k] == str(areacode)[k]:
                    areacounter += str(i)[k]
                    k += 1
                if areacounter == str(areacode):
                    finished_list.append(dict[i])
    return finished_list