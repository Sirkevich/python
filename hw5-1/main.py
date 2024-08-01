import keyword
import string

user_string = input("Enter your string: ")

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
string_punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^`{|}~"""
count = 0

result = True

for elem in user_string:

    if user_string[0] in numbers:
        result = False
        break

    if user_string in keyword.kwlist:
        result = False
        break

    if len(user_string) > 1 and user_string[1] == '_':
        result = False

    if elem == elem.capitalize() and False == (elem in numbers) and False == (elem in string.punctuation):
        result = False
        break

    if elem in string_punctuation:
        result = False
        break

print(result)
