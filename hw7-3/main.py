def second_index(text: str, some_str: str) -> int or None:

    result = None
    count = 0
    i = 0

    while i <= len(text):
        if text[i] == some_str[0]:
            result = i
            count += 1
        i += 1

        if count > 1:
            return result



res_string = second_index("Hello, hello", "lo")

print(res_string)