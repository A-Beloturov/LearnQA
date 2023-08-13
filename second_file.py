from typing import List, Callable


def func_a(x):
    print(f'В меня передали: {x}')


def func_b(*args):
    print(f'А в меня передали: {args}')


def func_c(*args):
    print(f'А я слива лиловая, спелая, садовая, с аргументами: {args}')


list_func: list = [func_a, func_b, func_c]

list_arg: list[tuple] = [('Proverka', 1, 2), (3, 4, 5), ("Абырвалг", "Мда..."), ("Жил черный волшебник, служивший луне")]


# def training_func(first_list, second_list):
#     for first in first_list:
#         first_result = []
#         for second in second_list:
#             first_result.append(first(*second))
#     return first_result


# def training_func(list_function: list[Callable], list_arguments: list[tuple]):
#     for func in list_function:
#         for arg in list_arguments:
#             try:
#                 func(*arg)
#             except TypeError:
#                 print("invalid argument for function")
#                 break
class InvalidSignatureError(Exception):
    def __init__(self, message="Invalid signature"):
        self.message = message
        super().__init__(self.message)

def training_func(list_function: list[Callable], list_arguments: list[tuple]):
    if len(list_function) != len(list_arguments):
        raise InvalidSignatureError
    for func, arg in zip(list_function, list_arguments):
        try:
            func(*arg)
        except TypeError:
            print('invalid argument for function')

training_func(list_func, list_arg)
