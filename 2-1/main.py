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
    Rock        = [A, X], [1 Point ]
    Paper       = [B, Y], [2 Points]
    Scissors    = [C, Z], [3 Points]
    Win         = [6 Points]
    Tie         = [3 Points]
    Loss        = [0 Points]

    Returns:
        int: An integer of total points
    """
    f = read_file("./data/input.txt")

    score = 0
    for line in f:
        you, me = line.split(" ")
        if you == chr(ord(me) + 9).upper():
            score += 3
        if me == "X":
            score += 1
            if you == "C":
                score += 6
        elif me == "Y":
            score += 2
            if you == "A":
                score += 6
        elif me == "Z":
            score += 3
            if you == "B":
                score += 6

    return score


def main():
    score = total_score()
    print(score)


if __name__ == "__main__":
    main()
