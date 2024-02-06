def filter_strings(input_array):
    output_array = []
    for string in input_array:
        if len(string) <= 3:
            output_array.append(string)
    return output_array

# Ввод массива с клавиатуры
input_array = input("Введите элементы массива через запятую: ").split(", ")

# Вызов функции для фильтрации массива
result_array = filter_strings(input_array)

if len(result_array) <= 3:
    # Вывод результата
    print(result_array)
else:
    # Вывод первых трех строк из отфильтрованного массива
    print(result_array[:3])
