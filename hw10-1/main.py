import math


def fact(user_number):
    return math.factorial(user_number)


def fact_gen(begin, end, func):
    """
    Generate factorials for the specified sequence of elements

    :param begin: first element of sequence
    :param end: count of elements of sequence
    :param func: function, which create elements for sequence
    :return: generator object
    """
    for elem in range(end):
        yield func(begin)
        begin += 1


value_list = list(fact_gen(2, 3, fact))

print(value_list)
