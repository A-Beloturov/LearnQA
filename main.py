

# def summy(*s):
#     a = 0
#     i = 0
#     while i < len(s):
#         a += s[i]
#         i+=1
#     return a
#
#
# def summa(*args):
#     print(sum(args))
#     return
#
# summa(2, 3, 4, 2, 10.2, 3)

# def dictionary(**kwargs):
#     dict_new = {}
#     for key, value in kwargs.items():
#         dict_new[key] = value
#     return dict_new
# print(dictionary(War='Piece', Freedom='Slavery', Ignorance='Strenght'))

def dictionary(**kwargs):
    dict_new = {key: value for key, value in kwargs.items()}
    return dict_new
print(dictionary(War='Piece', Freedom='Slavery', Ignorance='Strenght'))