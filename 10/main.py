def read_file(file: bytes) -> list:
    """
    Read a a text file and return a list of lines

    Args:
        file (bytes): A text file

    Returns:
        list: A list of lines from the file contents
    """
    with open(file) as f:
        lines = f.read().splitlines()
    return lines


def update_sprite(screen: list, register: int, current_cycle: int) -> None:
    row = 0
    for i in range(40, 240, 40):
        if current_cycle > i:
            row += 1
        else:
            break
    col = current_cycle - (40 * row) - 1
    if col in range(register - 1, register + 2):
        screen[row][col] = "#"


def main():
    """
    Run the program
    """
    input_file = "./data/input.txt"
    data = read_file(input_file)

    register = 1
    current_cycle = 0
    clock = {}

    screen = []
    for i in range(6):
        screen.append([])
        for _ in range(40):
            screen[i].append(" ")

    for line in data:
        current_cycle += 1
        update_sprite(screen, register, current_cycle)
        clock[current_cycle] = register
        if line != "noop":
            current_cycle += 1
            update_sprite(screen, register, current_cycle)
            clock[current_cycle] = register
            register += int(line.split()[1])

    total = 0
    for i in range(20, 221, 40):
        total += i * clock[i]
        print(f"{i}th cycle: Register = {clock[i]}; Signal Strength = {i * clock[i]}")

    print(f"Total Strength: {total}")

    for row in screen:
        print("".join(row))


if __name__ == "__main__":
    main()
