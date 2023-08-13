from typing import List, Callable


def func_a(*args):
    print(f'В меня передали: {args}')


def func_b(*args):
    print(f'А в меня передали: {args}')


def func_c(*args):
    print(f'А я слива лиловая, спелая, садовая, с аргументами: {args}')


list_func: list = [func_a, func_b, func_c]

x = "Проверка"
y = 7
z = 8

list_arg: list[tuple] = [(x, y, z)]


# def training_func(first_list, second_list):
#     for first in first_list:
#         first_result = []
#         for second in second_list:
#             first_result.append(first(*second))
#     return first_result


def training_func(list_function: list[Callable], list_arguments: list[tuple]):
    for func in list_function:
        for arg in list_arguments:
            func(*arg)


training_func(list_func, list_arg)
