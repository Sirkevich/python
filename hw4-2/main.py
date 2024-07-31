user_list = [0, 1, 7, 2, 4, 8]

i = 0
result = 0

if len(user_list) != 0:
    while i < len(user_list):
        if i % 2 == 0:
            result += user_list[i]
        i += 1
    result *= user_list[-1]

print(result)
