def is_even(digit: int) -> bool:
    """
    Checking if a number is even or not

    :param digit: integer number
    :return: a logical value depending on whether it is an even number
    """
    return True if digit % 2 == 0 else False


print(is_even(6))
