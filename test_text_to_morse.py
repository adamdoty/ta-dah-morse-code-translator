import pytest
from text_to_morse import is_text_convertible, prepare_text_to_convert, convert_to_morse


@pytest.mark.parametrize('text, expected', [
    ("PyBites is amazing!", True), ("Julian is all about mindset.", True), ("Bob sends me emails.", True),
    ("Be so good they can't ignore you - Steve Martin", True), ("#$@!%", False),
    ("['TalkPython', 'Real Python', 'MetaSnake', 'Reuven Lerner', 'PyBites', 'JetBrains']", False),
    ("“That'll do Donkey, that'll do.” – Shrek", False)
])
def test_is_text_convertible(text, expected):
    assert is_text_convertible(text) == expected


@pytest.mark.parametrize('text_to_convert, expected', [
    ("PyBites is amazing!",
     ['p', 'letter_space', 'y', 'letter_space', 'b', 'letter_space', 'i', 'letter_space', 't', 'letter_space', 'e',
      'letter_space', 's', 'word_space', 'i', 'letter_space', 's', 'word_space', 'a', 'letter_space', 'm',
      'letter_space', 'a', 'letter_space', 'z', 'letter_space', 'i', 'letter_space', 'n', 'letter_space', 'g',
      'letter_space', '!']),
    ("Julian is all about mindset.",
     ['j', 'letter_space', 'u', 'letter_space', 'l', 'letter_space', 'i', 'letter_space', 'a', 'letter_space', 'n',
      'word_space', 'i', 'letter_space', 's', 'word_space', 'a', 'letter_space', 'l', 'letter_space', 'l', 'word_space',
      'a', 'letter_space', 'b', 'letter_space', 'o', 'letter_space', 'u', 'letter_space', 't', 'word_space', 'm',
      'letter_space', 'i', 'letter_space', 'n', 'letter_space', 'd', 'letter_space', 's', 'letter_space', 'e',
      'letter_space', 't', 'letter_space', '.']),
    ("Bob sends me emails.",
     ['b', 'letter_space', 'o', 'letter_space', 'b', 'word_space', 's', 'letter_space', 'e', 'letter_space', 'n',
      'letter_space', 'd', 'letter_space', 's', 'word_space', 'm', 'letter_space', 'e', 'word_space', 'e',
      'letter_space', 'm', 'letter_space', 'a', 'letter_space', 'i', 'letter_space', 'l', 'letter_space', 's',
      'letter_space', '.']),
])
def test_prepare_text_to_convert(text_to_convert, expected):
    assert prepare_text_to_convert(text_to_convert) == expected


def test_convert_to_morse():
    assert convert_to_morse(
        ['p', 'letter_space', 'y', 'letter_space', 'b', 'letter_space', 'i', 'letter_space', 't', 'letter_space', 'e',
         'letter_space', 's', 'word_space', 'i', 'letter_space', 's', 'word_space', 'a', 'letter_space', 'm',
         'letter_space', 'a', 'letter_space', 'z', 'letter_space', 'i', 'letter_space', 'n', 'letter_space', 'g',
         'letter_space',
         '!']) == f".--.   -.--   -...   ..   -   .   ...       " \
                  f"..   ...       " \
                  f".-   --   .-   --..   ..   -.   --.   -.-.--"
