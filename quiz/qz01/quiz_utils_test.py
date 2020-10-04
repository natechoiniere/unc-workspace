"""Responses for Quiz 01. This is the test document."""


__author__ = "730443739"

import pytest
from quiz.qz01.quiz_utils import strs_to_floats, lookup, undelimit


def test_strs_floats() -> None:
    assert strs_to_floats(["3.14", "1.00", "2.33"]) == [3.14, 1.00, 2.33]
    assert strs_to_floats(["-3", "-1", "-2"]) == [-3.0, -1.0, -2.0]

def test_strs_to_floats_empty() -> None:
    assert strs_to_floats([]) == []


def test_lookup__unequal_length() -> None:
    """Tests that the function raises a value error when the lists have unequal lengths."""
    with pytest.raises(ValueError):
        lookup(["zero", "one"], [0, 0, 0], "zero")

    
def test_lookup_string_not_found() -> None:
    """Tests that the function returns a value error when the string isn't found in the first list."""
    with pytest.raises(ValueError):
        lookup(["pi", "e", "zero"], [3.14, 2.72, 0.0], "origin")


def test_lookup_empty() -> None:
    """Tests that the function returns a value error when the lists are empty."""
    with pytest.raises(ValueError):
        lookup([], [], "")


def test_undelimit_string() -> None:
    assert undelimit("one,two,three") == ['one', 'two', 'three']


def test_undelimit_edge() -> None:
    assert undelimit("one,,,two,,,three") == ['one', '', '', 'two', '', '', 'three']
    assert undelimit("123,345,678") == ['123', '345', '678']
    assert undelimit("") == ['']