# Copyright 2022, Adam Doty, All rights reserved.
# Program goal: takes any string input and converts it to morse code

# ---ADDITIONS CONSIDERED---
# write program foreword using conventions from itu pdf, note on spacing: 7 spaces v slash marks
# adjust letters to be consistent with itu pdf
# potential scope creep: save case of morse code translated within this program.
# optional decode/encode using slash marks in word spacing
# convert certain characters to similar other characters i.e. slanted quotes to quotation marks
# multiline string decode/encode
# simple gui
# complex gui/app
# use wikipedia ogg sound files to make actual audio morse code translations

# ---BUGS: 0---
# FIXED - issue with encoding this message: That'll do Donkey, that'll do.
#   The problem was the text_to_morse module's for loop was using indexing improperly.
#   This caused duplicate letters to be spaced improperly.

# FIXED - issue with comma replacement I switched , with * since * is not in the character dict
import text_to_morse as ttm
import morse_to_text as mtt

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
