def correct_sentence(text):
    result_text = text[0].capitalize() + text[1:]

    if result_text[-1] != '.':
        result_text += '.'

    print(result_text)


correct_sentence("greetings, friends")
