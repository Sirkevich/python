def second_index(text: str, some_str: str) -> int or None:

    index = text.find(some_str)
    index = text.find(some_str, index + 1)

    if index != -1:
        return index
    else:
        return None


res_string = second_index("Hello, hello", "lo")

print(res_string)
