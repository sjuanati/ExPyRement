"""
Argument unpacking in Python refers to a mechanism that allows you to use the 
contents of sequences and dictionaries as individual arguments in function calls.
This is achieved using the * (for sequences) and ** (for dictionaries) operators.
"""


def sum(a, b, c, d) -> int:
    sum = a + b + c + d
    print(f"{sum}")


def unpacking_args(*args, **kwargs):
    print(args) # shows (1, 2)
    print(kwargs) # shows {'c': 3, 'd': 4}


def test():
    # list unpacking
    list_args = [1, 2, 3, 4]
    sum(*list_args)

    # tuple unpacking
    tuple_args = (1, 2, 3, 4)
    sum(*tuple_args)

    # dictionary unpacking
    # argument names in function must be the same than key names in dictionary
    dict_args = {"a": 1, "b": 2, "c": 3, "d": 4}
    sum(**dict_args)

    # combined dictionary and list unpacking
    list_args2 = [1, 2]
    dict_args2 = {"c": 3, "d": 4}
    sum(*list_args2, **dict_args2)

    # unpacking in assignments -> shows 1 [2, 3] 4
    a, *b, c = [1, 2, 3, 4]
    print(a, b, c)

    # arguments are unpacked in the function
    unpacking_args(1, 2, c=3, d=4)
