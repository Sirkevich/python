import string

user_letters = input('Enter your letters: ')

first_letter = user_letters[0]
last_letter = user_letters[-1]

print(string.ascii_letters[string.ascii_letters.index(first_letter):string.ascii_letters.index(last_letter) + 1])
