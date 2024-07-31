user_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for elem in user_list:
    if elem == 0:
        user_list.remove(elem)
        user_list.append(elem)

print(user_list)
