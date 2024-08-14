def add_one(some_list):

    some_list_str = ''.join([str(elem) for elem in some_list])

    some_list_str = int(some_list_str) + 1

    result_lst = [int(elem) for elem in str(some_list_str)]

    return result_lst


result = add_one([9, 9, 9])

print(result)
