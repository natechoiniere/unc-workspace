"""Count the letters shakespeare used."""

from typing import Dict, List
from matplotlib import pyplot

READ_MODE = "r"
def main() -> None:
    """Entrypoint to our program."""
    letter_counts: Dict[str, int] = read_character_data("data/shakespeare.txt")
    chart_data(letter_counts)


def read_character_data(file: str) -> Dict[str, int]:
    """Given a filename, read its contents and count its characters."""
    counts: Dict[str, int] = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,}
    file_handle = open(file, READ_MODE)
    for line in file_handle:
        line = line.lower()
        for char in line:
            if char.isalpha():
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1
    file_handle.close() # Done working with file, close it.
    return counts


def chart_data(letter_counts: Dict[str, int]) -> None:
    """Plot the results of our textual analysis of Shakaespeare."""
    pyplot.title("Counts of Letters in Shakespeare")
    pyplot.xlabel("Letters")
    pyplot.ylabel("Count")

    labels: List[str] = list(letter_counts.keys())
    values: List[int] = list(letter_counts.values())
    pyplot.bar(labels, values)
    pyplot.show()

if __name__ == "__main__":
    main()