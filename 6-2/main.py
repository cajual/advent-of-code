# /usr/bin/env python

import re


def read_file(file) -> list:
    """
    Read in a file and return a list of lines

    Args:
        file (file): A test file

    Returns:
        list: A list of lines from a file
    """
    with open(file) as f:
        lines = f.read().splitlines()
    return lines


def decipher(marker) -> int:
    """
    Take an arbitrary list of alpha characters and find the first
    character position after a start marker of four continuous
    non-duplicate characters.

    Args:
        marker (int): The number of unique numbers required to mark

    Returns:
        int: Return the character position of the message start
    """
    f = read_file("./data/input.txt")

    for i in range(0, len(f[0]) - 4):
        string = sorted(set(f[0][i : i + marker]))
        if len(string) == marker:
            return i + marker


def main():
    code = decipher(14)
    print(code)


if __name__ == "__main__":
    main()
