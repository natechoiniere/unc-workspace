"""Exercise 05."""


__author__ = "730443739"


from typing import List


def count(int_list: List[int], given_num: int) -> int:
    """Returns the number of times the specified integer appears in a given list."""
    num_times: int = 0
    for i in int_list:
        if i == given_num:
            num_times += 1
    return num_times


def all(int_list: List[int], given_num: int) -> bool:
    """This function returns true if all numbers in the list are equal to the given integer."""
    num_times = 0
    if len(int_list) == 0:
        return False
    for i in int_list:
        if i == given_num:
            num_times += 1
    if num_times == len(int_list):
        return True
    else:
        return False


def max(int_list: List[int]) -> int:
    """Returns the value of the highest number in the list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")

    max_num: int = int_list[0]
    for i in int_list:
        if i > max_num:
            max_num = i
    return max_num


def is_equal(list1: List[int], list2: List[int]) -> bool:
    """Returns true if every element at every index of both lists is equal."""
    counter: int = 0
    ans: bool = False
    if list1 == [] and list2 == []:
        ans = True
    if len(list1) != len(list2):
        ans = False
    else:
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                counter += 1
        if counter == len(list1):
            ans = True
        elif counter != len(list1):
            ans = False
    return ans


def concat(list1: List[int], list2: List[int]) -> List[int]:
    """This function concatenates two lists."""
    concat_list: List[int] = []
    for i in range(len(list1)):
        concat_list.append(list1[i])
    for i in range(len(list2)):
        concat_list.append(list2[i])
    return concat_list


def sub(list: List[int], start: int, end: int) -> List[int]:
    """Returns a list of the elements in the given list between the given start and end indexes."""
    sub_list: List[int] = []
    if start < 0:
        for i in range(0, end):
            sub_list.append(list[i])
        return sub_list
    if end > len(list):
        for i in range(start, len(list) - 1):
            sub_list.append(list[i])
        return sub_list
    if len(list) == 0:
        return sub_list
    if start > len(list): 
        return sub_list
    if end <= 0:
        return sub_list
    for i in range(start, end):
        sub_list.append(list[i])
    return sub_list


def splice(list1: List[int], index: int, list2: List[int]) -> List[int]:
    """Returns a list with the second list spliced at the given index of the first list."""
    spliced_list: List[int] = []
    if index > len(list1):  # If index is greater than length of first list, put second list after first list.
        for i in range(len(list1)):
            spliced_list.append(list1[i])
        for i in range(len(list2)):
            spliced_list.append(list2[i])
        return spliced_list

    if index < 0:  # If index is negative, insert the second list before the first list.
        for i in range(len(list2)):
            spliced_list.append(list2[i])
        for i in range(len(list1)):
            spliced_list.append(list1[i])
        return spliced_list

    for i in range(len(list1)):  # If neither of the above edge cases are met.
        if i == index:
            for i in list2:
                spliced_list.append(i)
            spliced_list.append(list1[index])
        else:
            spliced_list.append(list1[i])
    return spliced_list