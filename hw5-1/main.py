import keyword
import string

user_string = input("Enter your string: ")

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
my_string_punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^`{|}~"""

result = True

if user_string[0] in numbers:
    result = False

if user_string in keyword.kwlist:
    result = False

if len(user_string) > 1 and user_string[1] == '_':
    result = False

for elem in user_string:

    if elem in my_string_punctuation:
        result = False
        break

    if elem == elem.capitalize() and False == (elem in numbers) and False == (elem in string.punctuation):
        result = False
        break

print(result)
