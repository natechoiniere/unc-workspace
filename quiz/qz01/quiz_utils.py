"""Responses for Quiz 01."""


__author__ = "730443739"

from typing import List


def strs_to_floats(string_list: List[str]) -> List[float]:
    """Converts a given list of string elements to a list of corresponding float elements."""
    new_list: List[float] = []
    for i in range(len(string_list)):
        new_list.append(float(string_list[i]))
    return new_list


def lookup(list1: List[str], list2: List[float], name: str) -> float:
    """Returns the float value from list2 that corresponds to the string value from list1."""
    counter: int = 0
    if (len(list1) != len(list2)):
        raise ValueError(name + " not found in first list, or lists have different lengths.")
    else:
        for i in range(len(list1)):
            if list1[i] == name:
                counter += 1
        if counter > 0:
            for i in range(len(list1)):
                if list1[i] == name:
                    return list2[i]
        elif counter == 0:
            raise ValueError(name + " not found in first list, or lists have different lengths.")
    return counter


def undelimit(string: str) -> List[str]:
    """Separates words in a string by commas, and puts those words into a list."""
    new_list: List[str] = []
    new_str: str = ""
    for i in string:
        if i != ",":
            new_str += i
        elif i == ",":
            new_list.append(new_str)
            new_str = ""
    new_list.append(new_str)
    return new_list


# def avg_column(List[str])