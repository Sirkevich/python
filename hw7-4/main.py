import random
#
#
# def common_elements():
#
#     first_list = [random.randint(1, 100) for i in range(random.randrange(1, 10, 3))]
#     second_list = [random.randint(1, 100) for i in range(random.randrange(1, 10, 5))]
#
#     set1 = set(first_list)
#     set2 = set(second_list)
#
#     intersection_set = set1.intersection(set2)
#
#     return intersection_set
#
#
# result = common_elements()
#
# print(result)

first_list = [random.randint(1, 100) for i in range(random.randrange(1, 10, 3))]
second_list = [random.randint(1, 100) for j in range(random.randrange(1, 10, 5))]

print(first_list)
print(second_list)

set1 = set(first_list)
set2 = set(second_list)

intersection_set = set1.intersection(set2)

print(intersection_set)