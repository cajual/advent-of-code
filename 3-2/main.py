#!/usr/bin/env python


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


def intersection(l1, l2, l3) -> list:
    """
    Take 3 lists and find the intersection between them

    Args:
        l1 (list): A list of N-elements
        l2 (list): A list of N-elements
        l3 (list): A list of N-elements

    Returns:
        list: A list coercion of a set of unique values
    """
    return list(set(l1) & set(l2) & set(l3))


def total_score() -> int:
    """
    Identify triplicate items across three rows, unique, and
    sum the values for each set.

    a-z = 1-26
    A-Z = 25-52

    Returns:
        int: An integer of total points
    """
    f = read_file("./data/input.txt")

    score = 0
    for i in range(len(f)):
        if i == 0 or i % 3 == 0:
            char = intersection(f[i], f[i + 1], f[i + 2])[0]
            modifier = 96
            if ord(char) < 91:
                modifier = 38
            score += ord(char) - modifier

    return score


def main():
    score = total_score()
    print(score)


if __name__ == "__main__":
    main()
