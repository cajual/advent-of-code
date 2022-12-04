# /usr/bin/env python


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


def check_lists() -> int:
    """
    Check for overlapping values within two lists of numbers where
    each list is separated by a comma and one list fully contains the
    numerical values of the other list.

    Returns:
        int: Total number of lines where one list contains the other
    """
    f = read_file("./data/input.txt")

    score = 0
    for line in f:
        a, b = line.split(",")
        a_min, a_max = [int(n) for n in a.split("-")]
        b_min, b_max = [int(n) for n in b.split("-")]
        if (a_min <= b_min and a_max >= b_max) or (b_min <= a_min and b_max >= a_max):
            score += 1

    return score


def main():
    score = check_lists()
    print(score)


if __name__ == "__main__":
    main()
