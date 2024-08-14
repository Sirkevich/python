import string


def is_palindrome(text):

    text = text.replace(' ', '').lower()
    new_text = ''

    for elem in text:
        if elem not in string.punctuation:
            new_text += elem

    return new_text == new_text[::-1]


result = is_palindrome('A man, a plan, a canal: Panama')

print(result)
