from morse_code_characters import morse_to_text_characters, morse_code_elements


def is_morse_code_convertible(morse_code: str) -> bool:
    morse_code = set(morse_code)
    for element in morse_code:
        if element in morse_code_elements.values():
            continue
        else:
            print(f'\n"{element}" is not a valid morse code element.')
            print(
                f'Try again. Please input a string with only the following elements:\n'
                f'{morse_code_elements}')
            return False
    return True


def prepare_morse_code_to_convert(morse_code: str) -> list:
    morse_code = morse_code.replace(morse_code_elements['medium_gap'], '* *')
    morse_code = morse_code.replace(morse_code_elements['short_gap'], '*')
    ready_to_convert = morse_code.split("*")
    return ready_to_convert


def convert_to_text(morse_code_to_convert: list) -> str:
    # print(morse_code_to_convert)
    converted_letters = [morse_to_text_characters[character] for character in morse_code_to_convert]
    morse_code_message = ''.join(converted_letters)
    return morse_code_message
