from typing import List

def main():
    pass

def fill_range(int1: int, int2: int) -> List[int]:
    totalList: List[int] = []
    if int1 < int2:
        for k in range (int1, int2):
            totalList.append(k)
            if k == (int2 - 1):
                totalList.append(k + 1)
    elif int1 > int2:  # For the edge case of int1 < int2
        for k in range (int2, int1):
            totalList.append(k)
            if k == (int1 - 1):
                totalList.append(k + 1)
    return totalList

if __name__ == "__main__":
    main()