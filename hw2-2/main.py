user_number = int(input("Enter your five-digit number "))

first_digit = str(user_number // 10000)
second_digit = str(user_number % 10000 // 1000)
third_digit = str(user_number % 1000 // 100)
fourth_digit = str(user_number % 100 // 10)
fifth_digit = str(user_number % 10)

result = int(fifth_digit + fourth_digit + third_digit + second_digit + first_digit)

print(result)
