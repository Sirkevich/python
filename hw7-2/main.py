def correct_sentence(text: str) -> str:
    result_text = text[0].capitalize() + text[1:]

    if result_text[-1] != '.':
        result_text += '.'

    return result_text


result = correct_sentence("greetings, Friends")

print(result)
