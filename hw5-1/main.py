import keyword
import string

user_string = input("Enter your string: ")

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

result = True
count = 0

if user_string[0] in numbers:
    result = False

if user_string in keyword.kwlist:
    result = False

if user_string.startswith('__'):
    result = False

for elem in user_string:

    if elem in string.punctuation and elem != '_':
        result = False
        break

    if elem == elem.capitalize() and elem not in numbers and elem not in string.punctuation:
        result = False
        break

print(result)
