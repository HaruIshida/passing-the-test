def filter_short_strings(strings):
    new_strings = []
    for string in strings:
        if len(string) <= 3:
            new_strings.append(string)
    return new_strings


def main():
    n = int(input("Введите количество строк: "))
    strings = []
    for _ in range(n):
        string = input("Введите строку: ")
        strings.append(string)

    filtered_strings = filter_short_strings(strings)

    print("Отфильтрованные строки:")
    for string in filtered_strings:
        print(string)


if __name__ == "__main__":
    main()

