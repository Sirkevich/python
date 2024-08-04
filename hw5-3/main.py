import string

user_string = input("Enter your string: ")
user_string = user_string.title()

for elem in user_string:
    if elem in string.punctuation or elem == ' ':
        user_string = user_string.replace(elem, '')

print(f'#{user_string[0:140]}')
