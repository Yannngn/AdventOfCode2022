points = {
    "A X": 1 + 3,
    "B Y": 2 + 3,
    "C Z": 3 + 3,
    "B X": 1 + 0,
    "C Y": 2 + 0,
    "A Z": 3 + 0,
    "C X": 1 + 6,
    "A Y": 2 + 6,
    "B Z": 3 + 6,
}


def main():
    current_value = 0
    with open("day_2/example.txt", "r") as file:
        for line in file:
            current_value += points[line.strip()]

    return current_value


if __name__ == "__main__":
    print(main())
