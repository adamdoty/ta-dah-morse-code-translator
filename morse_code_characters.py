text_to_morse_characters = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                            'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
                            'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
                            'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----',
                            '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                            '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                            '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
                            ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
                            '$': '...-..-', '@': '.--.-.', 'letter_space': '   ', 'word_space': '       '}

morse_code_prosigns = {'end_of_work': '...-.-', 'error': '........', 'invitation_to_transmit': '-.-',
                       'starting_signal': '-.-.-', 'new_page_signal': '.-.-.', 'understood': '...-.', 'wait': '.-...'}

morse_code_elements = {'short_mark': '.', 'long_mark': '-', 'inter-element_gap': ' ',
                       'short_gap': '   ', 'medium_gap': '       '}

morse_to_text_characters = {v: k for k, v in text_to_morse_characters.items()}
morse_to_text_characters.update({" ": " "})
