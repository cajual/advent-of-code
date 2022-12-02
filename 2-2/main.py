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
    Compare values in a list according to Rock, Paper, Scissors:
    Rock        = [A], [1 Point ]
    Paper       = [B], [2 Points]
    Scissors    = [C], [3 Points]
    Win         = [Z], [6 Points]
    Tie         = [Y], [3 Points]
    Loss        = [X], [0 Points]

    Returns:
        int: An integer of total points
    """
    f = read_file("./data/input.txt")

    strategy = {
        "X": {
            "A": 3,
            "B": 1,
            "C": 2,
        },
        "Y": {
            "A": 1,
            "B": 2,
            "C": 3,
        },
        "Z": {
            "A": 2,
            "B": 3,
            "C": 1,
        },
    }

    score = 0
    for line in f:
        you, outcome = line.split(" ")
        if outcome == "X":
            score += strategy[outcome][you]
        elif outcome == "Y":
            score += strategy[outcome][you] + 3
        elif outcome == "Z":
            score += strategy[outcome][you] + 6

    return score


def main():
    score = total_score()
    print(score)


if __name__ == "__main__":
    main()
