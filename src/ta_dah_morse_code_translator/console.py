import click
from ta_dah_morse_code_translator import text_to_morse as ttm, morse_to_text as mtt

from . import __version__, morse_code_characters


@click.command()
@click.version_option(version=__version__)
def main():
    """The Ta Dah Morse Code Translator project."""
    click.echo("Hello world!")
    selection = input("Type 'm' to convert text to morse code or type 't' to convert morse code to text: ").lower()
    if selection == 'm':
        encode()
    elif selection == 't':
        decode()
    else:
        print("Invalid input. Please select from the listed options.")
        main()
    if input("Would you like to encode or decode again? 'y' or 'n': ").lower() == "y":
        main()


def encode():
    message = input("Please input the text you want encode:\n")
    if ttm.is_text_convertible(message):
        convertible_message = ttm.prepare_text_to_convert(message)
        converted_message = ttm.convert_to_morse(convertible_message)
        print(converted_message)
    else:
        main()


def decode():
    message = input("Please input the morse code you want to convert to text:\n").lower()
    if mtt.is_morse_code_convertible(message):
        convertible_message = mtt.prepare_morse_code_to_convert(message)
        converted_message = mtt.convert_to_text(convertible_message)
        print(converted_message)
    else:
        main()
