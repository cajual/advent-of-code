# /usr/bin/env python

from __future__ import annotations
from typing import TypedDict
import uuid


class Node(TypedDict):
    name: str
    size: int
    directory: bool
    parent: Node
    children: dict


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


def dir_size(disk_size, required_space) -> int:
    """
    Given a text file input of simulated directory commands and folder
    structures, find the size of all files and recursively add to each
    parent folder

    Args:
        disk_size (int): Total size of the simulated disk
        required_space (int): Total space required for the simulated file

    Returns:
        int: Return the smallest directory size that may be deleted to
             free up enough space for the installation
    """
    f = read_file("./data/input.txt")

    seen = {}
    root: Node = dict(name="root", size=0, directory=True, parent=None, children={})
    seen[uuid.uuid1()] = root
    current = root
    for line in f:
        args = line.split(" ")
        if args[1] == "ls":
            pass
        elif args[1] == "cd":
            location = args[2] if args[2] != "/" else "root"
            if location == "root":
                pass
            elif location == "..":
                current = current["parent"]
            else:
                current = current["children"][location]
        elif args[0] == "dir":
            name = args[1]
            if not current["children"].get(name):
                node: Node = dict(
                    name=name, size=0, directory=True, parent=current, children={}
                )
                seen[uuid.uuid1()] = node
                current["children"][name] = node
        else:
            size = int(args[0])
            filename = args[1]
            if not current["children"].get(filename):
                node: Node = dict(
                    name=filename, size=size, directory=False, parent=current
                )
                current["children"][filename] = node
                n = current
                while True:
                    n["size"] += size
                    n = n["parent"]
                    if not n:
                        break

    if (disk_size - root["size"]) >= required_space:
        return 0

    total = float('+inf')
    for _, v in seen.items():
        if v["size"] >= (required_space - (disk_size - root["size"])):
            if v["size"] < total:
                total = v["size"]

    return total


def main():
    total = dir_size(70000000, 30000000)
    print(total)


if __name__ == "__main__":
    main()
