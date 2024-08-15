def find_unique_value(some_list: list):
    for elem in some_list:
        if some_list.count(elem) == 1:
            return elem


result = find_unique_value([5, 5, 5, 2, 2, 0.5])

print(result)
