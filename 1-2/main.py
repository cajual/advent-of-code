#!/usr/bin/env python

from itertools import groupby


def top_three(file) -> None:
    """
    Print the top three total values of a 2d list

    Args:
        file (file): Relative path to a text file
    """
    with open(file) as f:
        lines = f.read().splitlines()

    superset = [list(j) for i, j in groupby(lines, key=bool) if i]

    top = []
    for x in superset:
        x = [eval(i) for i in x]
        top.append(sum(x))
    top.sort(reverse=True)

    print(sum(top[:3]))


def main():
    top_three("./data/input.txt")


if __name__ == "__main__":
    main()
