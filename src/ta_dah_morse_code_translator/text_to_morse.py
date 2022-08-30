from morse_code_characters import text_to_morse_characters

special_characters = [' ']
morse_alphabet_characters_ext = [key for key in text_to_morse_characters if len(key) == 1] + special_characters


def is_text_convertible(text: str) -> bool:
    text = text.lower()
    for character in set(text):
        if character in text_to_morse_characters:
            continue
        elif character in special_characters:
            continue
        else:
            print(f'\n"{character}" is not a valid character.')
            print(
                f'Try again. Please input a string with only the following characters:\n'
                f'{" ".join(morse_alphabet_characters_ext[:-2])} whitespace')
            return False
    return True


def prepare_text_to_convert(text: str) -> list:
    text = text.lower()
    text = text.replace(" ", "* *")
    text = text.split("*")
    text_records = [[record] for record in text]
    ready_to_convert = []
    for record in text_records:
        record = record[0]
        if len(record) > 1:
            for character_index in range(len(record)):
                character = record[character_index]
                if character_index < len(record) - 1:
                    ready_to_convert.append(character)
                    ready_to_convert.append("letter_space")
                else:
                    ready_to_convert.append(character)
            # add letter_space btw letters
            # return a list of characters + letter_space
        elif record == " ":
            record = "word_space"
            ready_to_convert.append(record)
        else:
            ready_to_convert.append(record)
    return ready_to_convert


def convert_to_morse(text_to_convert: list) -> str:
    converted_letters = [text_to_morse_characters[character] for character in text_to_convert]
    morse_code_message = ''.join(converted_letters)
    return morse_code_message
