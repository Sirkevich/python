def common_elements():

    first_list = set([x for x in range(100) if x % 3 == 0])
    second_list = set([x for x in range(100) if x % 5 == 0])

    intersection_set = first_list.intersection(second_list)

    return intersection_set


result = common_elements()

print(result)
