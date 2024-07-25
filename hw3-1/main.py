first_user_number = int(input('Enter first number: '))
second_user_number = int(input('Enter second number: '))
math_operation = input('Enter math operation: ')

result = 0

if math_operation == '+':
    result = first_user_number + second_user_number
elif math_operation == '-':
    result = first_user_number - second_user_number
elif math_operation == '*':
    result = first_user_number * second_user_number
elif math_operation == '/':
    if second_user_number != 0:
        result = first_user_number / second_user_number
    else:
        result = 'division by 0 is impossible'

print(result)