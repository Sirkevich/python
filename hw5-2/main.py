
while True:
    result = 0
    first_user_number = int(input('Enter first number: '))
    second_user_number = int(input('Enter second number: '))
    math_operation = input('Enter math operation: ')

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

    print('Your result:', result)
    request_to_user = input('Would you like to continue the calculations? (y/n): ')

    if request_to_user != 'y' and request_to_user != 'Y':
        print('Goodbye')
        break
