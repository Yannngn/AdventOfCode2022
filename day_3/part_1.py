import string

POS = " " + string.ascii_lowercase + string.ascii_uppercase


def main():
    current_value = 0
    with open("day_3/input.txt", "r") as file:
        for line in file:
            sack = line.strip()
            sack_size = len(sack)
            c1, c2 = sack[: sack_size // 2], sack[sack_size // 2 :]

            for letter in set(c1):
                if letter in set(c2):
                    current_value += POS.index(letter)

    return current_value


if __name__ == "__main__":
    print(main())
