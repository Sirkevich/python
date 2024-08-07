import string

user_letters = input('Enter your letters: ')

lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


user_letters = user_letters.split('-')
user_letters = ''.join(user_letters)


first_letter = ord(user_letters[0])
second_letter = ord(user_letters[1])
result = ''

if first_letter < second_letter:
    while first_letter <= second_letter:
        result += (chr(first_letter))
        first_letter += 1

else:
    while second_letter <= 65:
        result += (chr(second_letter))
        second_letter -= 1
    result = lower_letters + result

print(result)

print(string.ascii_letters)

print(ord('a'))
print(ord('Z'))
# for let in string.ascii_letters:
#     i = user_letters[0]
#     if let !=
#     result = ''


