

def difference(*args: int or float) -> int or float:
    numbers_list = []

    for elem in args:
        numbers_list.append(elem)

    if numbers_list:
        diff = round(max(numbers_list) - min(numbers_list), 2)

    else:
        diff = 0

    return diff


result = difference(0)

print(result)
