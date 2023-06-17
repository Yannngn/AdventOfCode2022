score = {"A": 1, "B": 2, "C": 3}

response = {
    "A X": "A C",
    "A Y": "A A",
    "A Z": "A B",
    "B X": "B A",
    "B Y": "B B",
    "B Z": "B C",
    "C X": "C B",
    "C Y": "C C",
    "C Z": "C A",
}

points = {
    "A A": 1 + 3,
    "A B": 2 + 6,
    "A C": 3 + 0,
    "B A": 1 + 0,
    "B B": 2 + 3,
    "B C": 3 + 6,
    "C A": 1 + 6,
    "C B": 2 + 0,
    "C C": 3 + 3,
}


def main():
    current_value = 0
    with open("day_2/input.txt", "r") as file:
        for line in file:
            current_value += points[response[line.strip()]]

    return current_value


if __name__ == "__main__":
    print(main())
