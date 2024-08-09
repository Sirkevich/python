user_number = int(input('Enter your integer number: '))
result = 1

while user_number > 9:
    for i in str(user_number):
        result *= int(i)
    user_number = result
    result = 1

print(user_number)
