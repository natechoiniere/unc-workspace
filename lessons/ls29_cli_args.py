"""Lesson 29, Command-Line Interface Arguments in Python's sys.argv"""

import sys

from typing import List

args: List[str] = sys.argv

print(len(sys.argv))
print(args[1])
print(args[2])