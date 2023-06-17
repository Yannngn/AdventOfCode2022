def main():
    result_list = []
    current_value = 0
    with open("day_1/input.txt", "r") as file:
        for line in file:
            try:
                current_value += int(line.strip())
            except ValueError:
                result_list.append(current_value)
                current_value = 0

        return max(result_list)


if __name__ == "__main__":
    print(main())
