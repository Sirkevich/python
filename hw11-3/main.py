from inspect import isgenerator


def is_even(digit: int) -> bool:
    """
    Checking if a number is even or not

    :param digit: integer number
    :return: a logical value depending on whether it is an even number
    """
    return (digit & 1) == 0


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

print('ok')
