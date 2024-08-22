import string


def first_word(text: str) -> str:
    """
     Found first word in string

    :param text: entered string
    :return: first word in string
    """
    for elem in text:
        if elem in string.punctuation and elem != "'":
            text = text.replace(elem, ' ')

    string_list = text.split()

    return string_list[0]


print(first_word("greetings, friends"))
