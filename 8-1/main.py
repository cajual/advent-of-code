# /usr/bin/env python

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    height: int
    visible: bool
    west: list
    east: list
    north: list
    south: list


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


def visible() -> int:
    """
    Provided a grid structure of single-digit integers as both a position
    and a height for a Point, calculate the number of points that are
    visible from any side of the grid.

    Returns:
        int: Returns the total number of visible points
    """
    row = read_file("./data/input.txt")
    col = list(''.join(x) for x in zip(*row))

    trees = []
    for y in range(len(row)):
        for x in range(len(row[y])):
            trees.append(
                Point(
                    x=x,
                    y=y,
                    height=row[y][x],
                    visible=False,
                    west=row[y][:x],
                    east=row[y][x+1:len(row[y])],
                    north=col[x][:y],
                    south=col[x][y+1:len(col)],
                )
            )

    visible = 0
    for tree in trees:
        for direction in [tree.north, tree.east, tree.south, tree.west]:
            if len(direction) == 0 or tree.height > max(direction):
                tree.visible = True
        if tree.visible == True:
            visible += 1

    return visible


def main():
    total = visible()
    print(total)


if __name__ == "__main__":
    main()
