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


def decipher() -> int:
    """
    Take an arbitrary list of alpha characters and find the first
    character position after a start marker of four continuous
    non-duplicate characters.

    Returns:
        int: Return the character position of the message start
    """
    f = read_file("./data/input.txt")

    for i in range(0, len(f[0]) - 4):
        string = sorted(set(f[0][i:i+4]))
        if len(string) == 4:
            return i + 4


def main():
    code = decipher()
    print(code)


if __name__ == "__main__":
    main()
