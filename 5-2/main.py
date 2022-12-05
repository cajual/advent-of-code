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


def update_stack(line, stack) -> None:
    """
    Given an UTF-8 text file with a columnar store of known dimentions
    store the appropriate values in a dict, excluding empty values

    Note: Updates in place

    Args:
        line (str): The current line of a read file as a string
        stack (dict): An existing dictionary of columnar lists

    """
    col = 1
    for i in range(0, len(line)):
        if line[i].isalpha():
            if not stack.get(col):
                stack[col] = []
            stack[col].insert(0, line[i])
        elif (i + 1) % 4 == 0:
            col += 1


def order_stack() -> list:
    """
    Take directions to move elements from one list to another and return
    the top item of each list

    Directions are structured as: "move X from Y to Z"

    Caveat: Move all items together at once

    Returns:
        int: The last (top) item of each list
    """
    f = read_file("./data/input.txt")

    stack = {}
    for line in f:
        if re.match("^move", line):
            vals = re.match(".*?(\d+).*?(\d+).*?(\d+)", line).groups()
            vals = [eval(x) for x in vals]
            stack[vals[2]] += stack[vals[1]][len(stack[vals[1]]) - vals[0] : len(stack[vals[1]])]
            stack[vals[1]] = stack[vals[1]][: len(stack[vals[1]]) - vals[0]]
        else:
            update_stack(line, stack)

    top = []
    for k in sorted(stack):
        top.append(stack[k][len(stack[k]) - 1])

    return top


def main():
    stack = order_stack()
    print(stack)


if __name__ == "__main__":
    main()
