import string

POS = " " + string.ascii_lowercase + string.ascii_uppercase


def main():
    current_value = 0
    count = 1
    with open("day_3/input.txt", "r") as file:
        file_iter = iter(file)

        common_chars = set(next(file_iter).strip())
        for line in file_iter:
            if count % 3 == 0:
                current_value += POS.index(common_chars.pop())

                common_chars = set(line.strip())
                count = 1
                continue

            common_chars = common_chars.intersection(set(line.strip()))
            count += 1

        current_value += POS.index(common_chars.pop())

    return current_value


if __name__ == "__main__":
    print(main())
