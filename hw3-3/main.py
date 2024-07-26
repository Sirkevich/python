user_list = []
result_list = []

middle_of_list = int(len(user_list) / 2)

if len(user_list) == 0:
    result_list = [[], []]

elif len(user_list) % 2 == 0:
    result_list = [user_list[:middle_of_list], user_list[middle_of_list:]]

else:
    result_list = [user_list[:middle_of_list + 1], user_list[middle_of_list + 1:]]

print(result_list)
