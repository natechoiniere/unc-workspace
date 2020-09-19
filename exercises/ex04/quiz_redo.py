"""Redoing some QZ00 problems."""


__author__ = "730443739"


def is_tar(string: str) -> bool:
    """This method returns true if the string begins with t and ends with r."""
    if string == "":
        return False
    elif (string[0] == "t") and (string[len(string) - 1] == "r"):
        return True
    else:
        return False


def boot(string: str, int1: int, int2: int) -> str:
    """This method 'boots' the integers int1 through int2 from the given string."""
    booted_str: str = ""
    i: int = 0
    while i < len(string):
        char: str = string[i]
        if i < int1 or i > int2:
            booted_str += char
        i = i + 1
    return booted_str


def sum_inputs() -> str:
    """This method sums the given inputs."""
    num: int = int(input("Enter an int, -1 to sum: "))
    tally: int = num
    while num != -1:
        num = int(input("Enter an int, -1 to sum: "))
        tally += num
    ans: str = "Sum is " + str(tally + 1)
    return ans


def strip(string: str, side: str) -> str:
    """This function strips the string on either the left or right side."""
    if (side == "left" or "right"):
        if(side == "left"):
            i = 0
            stripped_str: str = ""
            while i < len(string):
                if string[i] != " ":
                    stripped_str += string[i]
                i = i + 1
            return stripped_str
        if(side == "right"):
            i = 0
            stripped_str = ""
            while i < len(string):
                if string[i] != " ":
                    stripped_str += string[i]
                i = i + 1
            return stripped_str
    else:
        print("Select either left or right for your side.")
    return string