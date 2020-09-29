from typing import List
from lessons.ls24_module import fill_range

def test_fill_range_use_case_0() -> None:
    low: int = 1
    high: int = 3
    expected_result: List[int] = [1, 2, 3]
    assert fill_range(low, high) == expected_result
    assert len(fill_range(low, high)) == len(expected_result)

def test_fill_range_edge_case_0() -> None:
    low: int = 3
    high: int = 1
    expected_result: List[int] = [1, 2, 3]
    assert fill_range(low, high) == expected_result