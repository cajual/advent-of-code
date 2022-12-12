def data(file: bytes) -> list:
    """
    Accept a file and return the conents as a list of lines

    Args:
        file (bytes): _description_

    Returns:
        list: Each line of the file as a list element
    """
    with open(file) as f:
        lines = f.read().splitlines()
    return lines


def get_vector_change(direction: str) -> None:
    """
    Accept a direction and match it against a known list of directions

    Args:
        direction (str): A known direction as (U)p, (D)own, (L)eft, (R)ight
    """
    match direction:
        case "L":
            return [-1, 0]
        case "U":
            return [0, 1]
        case "R":
            return [1, 0]
        case "D":
            return [0, -1]
        case _:
            print("Invalid direction argument")
            exit(-1)


def move_tail(head: list[int], tail: list[int]) -> None:
    """
    Moves the tail object in coordination with any preceding nodes (head)

    Args:
        head (list[int]): The leading node as a list of coordinates
        tail (list[int]): The lagging node as a list of coordinates
    """
    d = [x - y for x, y in zip(head, tail)]

    if abs(d[0]) > 1 or abs(d[1]) > 1:
        tail[:] = [
            n1 + (1 if n2 >= 1 else -1 if n2 <= -1 else 0) for n1, n2 in zip(tail, d)
        ]


def main():
    """
    Run the program
    """
    input = [
        (line.split()[0], int(line.split()[1])) for line in data("./data/input.txt")
    ]

    head = [0, 0]
    tail = [0, 0]

    tail_parts = [[0, 0] for _ in range(9)]

    visited_p1 = set()
    visited_p2 = set()

    for direction, amount in input:
        for i in range(amount):
            head = [x + y for x, y in zip(head, get_vector_change(direction))]

            move_tail(head, tail)
            visited_p1.add(tuple(tail))

            for i in range(len(tail_parts)):
                move_tail(head if i == 0 else tail_parts[i - 1], tail_parts[i])

                if i == 8:
                    visited_p2.add(tuple(tail_parts[i]))

    print(f"Part 1: {len(visited_p1)}")
    print(f"Part 2: {len(visited_p2)}")


if __name__ == "__main__":
    main()
