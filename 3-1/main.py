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


def total_score() -> int:
    """
    Identify duplicate items based on a weighted scale and sum
    the totals of those items.

    a-z = 1-26
    A-Z = 25-52

    Returns:
        int: An integer of total points
    """
    f = read_file("./data/input.txt")

    score = 0
    for i in range(len(f)):
        for item in f[i][: len(f[i]) // 2]:
            if item in f[i][len(f[i]) // 2 :]:
                modifier = 96
                if ord(item) < 91:
                    modifier = 38
                score += ord(item) - modifier
                break

    return score


def main():
    score = total_score()
    print(score)


if __name__ == "__main__":
    main()
