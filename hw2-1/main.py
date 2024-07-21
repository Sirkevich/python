user_number = int(input("Enter your four-digit number "))

first_digit = user_number // 1000
second_digit = user_number % 1000 // 100
third_digit = user_number % 100 // 10
fourth_digit = user_number % 10

print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)
