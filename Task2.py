# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiply_of_pars(origin_list: list):
    result = list()
    repeats = len(origin_list) // 2 if len(origin_list) % 2 == 0 else len(origin_list) // 2 + 1
    for i in range(repeats):
        result.append(origin_list[i] * origin_list[len(origin_list) - (i + 1)])
    return result


test1 = [2, 3, 4, 5, 6]
print(multiply_of_pars(test1))
test2 = [2, 3, 5, 6]
print(multiply_of_pars(test2))