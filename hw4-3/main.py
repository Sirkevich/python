import random

data_list = [random.randint(1, 10) for i in range(random.randint(3, 10))]
result_list = [data_list[0], data_list[2], data_list[-2]]

print(data_list)
print(result_list)
