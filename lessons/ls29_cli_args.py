"""Lesson 29, Command-Line Interface Arguments in Python's sys.argv"""

import sys

from typing import List, Dict


# Run our program as a module with two command-line arguments:
# 1. Name of the file to search
# 2. Search term we're looking for
# Print out all lines containing the search term and the total
# number of matches.


def main() -> None:
    """Entry point of the program."""
    args: Dict[str, str] = read_args()
    results: List[str] = search_file(args["file_path"], args["keyword"])
    show_results(results)

def read_args() -> Dict[str, str]:
    """Check for valid command line arguments and return them in a dictionary."""
    if len(sys.argv) != 3:
        print("Usage: python -m lessons.ls29_cli_args [FILE] [KEYWORD]")
        exit()
    return {"file_path": sys.argv[1], "keyword": sys.argv[2]}


def show_results(matches: List[str]) -> None:
    """Print out matching lines and total number of matches."""
    for line in matches:
        print(line.strip())
    print(f"Total matches: {len(matches)}")


def search_file(file_path: str, keyword: str) -> List[str]:
    """Opens file_path, reads each line, returns a list of lines w/ keyword."""
    matches: List[str] = []
    file_handle = open(file_path, "r", encoding="utf8")
    for line in file_handle:
        if keyword in line:  # Can also use if line.index(keyword) >= 0:
            matches.append(line)
    file_handle.close()
    return matches

    
if __name__ == "__main__":
    main()