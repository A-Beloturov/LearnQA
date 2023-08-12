def func_a(*args):
    print(sum(args))


def func_b(*args):
    print(f'В меня передали: {args}')


def func_c(*args):
    print(f'А в меня передали: {args}')


list_func = [func_a(), func_b(), func_c()]

x = 6
y = 6
z = 6

list_arg = [x, y, z]


def training_func(first_list, second_list):
    pass

# training_func(list_func, list_arg)
