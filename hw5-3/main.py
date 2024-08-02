import string

user_string = ('This is a sample string that contains exactly one hundred and forty characters. It includes spaces and '
               'punctuation as part of the total character cot.This is a sample string that contains exactly one '
               'hundred and  forty characters. It includes spaces and'
               'punctuation as part of the total character cot.')
# input("Enter your string: "))
print(len(user_string))
data = user_string.split()

result_string = ''

for elem in data:
    elem = elem.capitalize()
    result_string += elem

for elem in result_string:
    if elem in string.punctuation or elem == ' ':
        result_string = result_string.replace(elem, '')
    else:
        continue

print(data)
print(len(result_string))
print(f'#{result_string}')
