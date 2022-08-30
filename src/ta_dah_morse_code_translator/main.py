# Copyright 2022, Adam Doty, All rights reserved.
# Program goal: takes any string input and converts it to morse code

# ---ADDITIONS CONSIDERED---
# add note on spacing: 7 spaces v slash marks
# potential scope creep: save letter casing of morse code translated within this program.
# optional decode/encode using slash marks inplace of word spacing
# convert certain characters to similar other characters i.e. slanted quotes to quotation marks
# multiline string decode/encode
# simple gui
# complex gui/app
# use wikipedia ogg sound files to make actual audio morse code translations

from ta_dah_morse_code_translator import text_to_morse as ttm, morse_to_text as mtt

is_program_running = True
while is_program_running:
    selection = input("Type 'm' to convert text to morse code or type 't' to convert morse code to text: ").lower()
    if selection == 'm':
        message = input("Please input the text you want encode:\n")
        if ttm.is_text_convertible(message):
            convertible_message = ttm.prepare_text_to_convert(message)
            converted_message = ttm.convert_to_morse(convertible_message)
            print(converted_message)
        else:
            continue
    elif selection == 't':
        message = input("Please input the morse code you want to convert to text:\n").lower()
        if mtt.is_morse_code_convertible(message):
            convertible_message = mtt.prepare_morse_code_to_convert(message)
            converted_message = mtt.convert_to_text(convertible_message)
            print(converted_message)
        else:
            continue
    else:
        print("Invalid input. Please select from the listed options.")
        continue
    if input("Would you like to encode or decode again? 'y' or 'n': ").lower() == "y":
        continue
    else:
        break
