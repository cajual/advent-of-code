#!/usr/bin/env python

from itertools import groupby


def max_value(file) -> None:
    """
    Print the max total value of a 2d list

    Args:
        file (file): Relative path to a text file
    """
    with open("./data/input.txt") as f:
        lines = f.read().splitlines()

    superset = [list(j) for i, j in groupby(lines, key=bool) if i]

    mx = 0
    for x in superset:
        x = [eval(i) for i in x]
        if sum(x) > mx:
            mx = sum(x)

    print(mx)


def main():
    max_value("./data/input.txt")


if __name__ == "__main__":
    main()
