"""Test file for utils.py."""


__author__ = "730443739"

import pytest
from typing import List
from exercises.ex05.utils import count, all, max, is_equal, concat, sub, splice


def test_count_one() -> None:
    """Test counting a single instance of the needle in the haystack."""
    assert count([1, 1, 0, 1, 20, 100], 0) == 1


def test_count_neg() -> None:
    """Test counting negative numbers."""
    assert count([1, -1], -1) == 1


def test_count_none() -> None:
    """Test the result for count when there is no number in the list."""
    assert count([1, 3, 5], 7) == 0


def test_all_true() -> None:
    """Test the result for all when true."""
    assert all([1, 1, 1], 1)


def test_all_false() -> None:
    """Test the result for all when false."""
    assert not all([1, 2, 3], 1)


def test_all_empty() -> None:
    """Tests that the all function returns False if the list is empty."""
    assert not all([], 2)


def test_max_() -> None:
    """Test the result for max."""
    assert max([0, 1, 2, 3, 2, 8, 3]) == 8


def test_max_of_empty() -> None:
    """Calling the 'max' function with an empty list should raise a Value Error."""
    with pytest.raises(ValueError):
        empty_list: List[int] = []
        max(empty_list)

    
def test_max_is_neg() -> None:
    """Calling the 'max' function with all negatives should return a negative number."""
    assert max([-3, -6, -1]) == -1


def test_is_equal() -> None:
    """Tests whether the function returns true if the lists are equal, and false if they're not."""
    assert is_equal([1, 0, 1], [1, 0, 1]) and not is_equal([1, 0, 1], [1, 1, 0])


def test_is_equal_length() -> None:
    """Tests that the function returns false if the lists are of unequal length."""
    assert not is_equal([1, 0, 3, 4], [1, 2])


def test_concat_empty() -> None:
    """Tests that an empty list will be concatenated properly."""
    assert concat([], []) == []
    assert concat([], [1, 2]) == [1, 2]
    assert concat([1, 2], []) == [1, 2]


def test_sub_empty() -> None:
    """Tests that an empty list will return empty."""
    assert sub([], 1, 2) == []


def test_sub_high_end() -> None:
    """Tests that the function uses the end of the list if end > len(list)."""
    assert sub([1, 2, 3], 0, 4) == [1, 2]


def test_sub_neg_start() -> None:
    """Tests that the function starts from the 0 index if start < 0."""
    assert sub([1, 2, 3], -2, 2) == [1, 2]


def test_splice_empty() -> None:
    """Tests that the function will splice correctly for an empty list."""
    assert splice([], 2, [1, 2]) == [1, 2]


def test_splice_neg() -> None:
    """Tests that the function will append the splice list to the end of the second list if the index is negative."""
    assert splice([1, 2, 2], -2, [0, 1, 2]) == [0, 1, 2, 1, 2, 2]


def test_splice_high_index() -> None:
    """Tests that the function will splice the second list to the end of the first list of the index > len(list1)."""
    assert splice([0, 1, 2], 4, [2, 3]) == [0, 1, 2, 2, 3]