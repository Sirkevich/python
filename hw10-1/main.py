from inspect import isgenerator


def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    """
    Generate factorials for the specified sequence of elements

    :param begin: first element of sequence
    :param end: count of elements of sequence
    :param func: function, which create elements for sequence
    :return: generator object
    """
    for elem in range(end):
        yield begin
        begin = func(begin)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
