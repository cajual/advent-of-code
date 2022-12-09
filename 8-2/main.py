# /usr/bin/env python

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    height: int
    view: int
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


def distance() -> int:
    """
    Provided a grid structure of single-digit integers as both a position
    and a height for a Point, calculate the number points in each direction
    which the given point is larger than, inclusive of an equal or larger
    point, then multiple the views for total view distance.

    Returns:
        int: Returns the total view area of a gride of points
    """
    row = read_file("./data/input.txt")
    col = list("".join(x) for x in zip(*row))

    trees = []
    for y in range(len(row)):
        for x in range(len(row[y])):
            trees.append(
                Point(
                    x=x,
                    y=y,
                    height=row[y][x],
                    view=0,
                    west=row[y][:x],
                    east=row[y][x + 1 : len(row[y])],
                    north=col[x][:y],
                    south=col[x][y + 1 : len(col)],
                )
            )

    total = 0
    for tree in trees:
        distance = 1
        for direction, neighbors in {
            "north": tree.north,
            "east": tree.east,
            "south": tree.south,
            "west": tree.west,
        }.items():
            if not neighbors:
                continue
            if tree.height > max(neighbors):
                distance *= len(neighbors)
                continue
            if direction in ["north", "west"]:
                neighbors = neighbors[::-1]
            for i in range(len(neighbors)):
                if neighbors[i] >= tree.height:
                    distance *= i + 1
                    break
        tree.view = distance
        if tree.view > total:
            total = tree.view

    return total


def main():
    total = distance()
    print(total)


if __name__ == "__main__":
    main()
