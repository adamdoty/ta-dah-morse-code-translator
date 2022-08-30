import pytest
from morse_to_text import is_morse_code_convertible, prepare_morse_code_to_convert, convert_to_text


# convert these text into morse code
@pytest.mark.parametrize('morse_code, expected', [
    (".--.   -.--   -...   ..   -   .   ...       ..   ...       .-   --   .-   --..   ..   -.   --.   -.-.--", True),
    ("-...   ---   -...       ...   .   -.   -..   ...       --   .       .   --   .-   ..   .-..   ...   .-.-.-", True)
])
def test_is_morse_code_convertible(morse_code: str, expected: bool):
    assert is_morse_code_convertible(morse_code) == expected


@pytest.mark.parametrize('morse_code, expected', [
    (".--.   -.--   -...   ..   -   .   ...       ..   ...       .-   --   .-   --..   ..   -.   --.   -.-.--",
     [".--.", "-.--", "-...", "..", "-", ".", "...", " ", "..", "...", " ", ".-", "--", ".-", "--..", "..", "-.", "--.",
      "-.-.--"]),
    ("-...   ---   -...       ...   .   -.   -..   ...       --   .       .   --   .-   ..   .-..   ...   .-.-.-",
     ["-...", "---", "-...", " ", "...", ".", "-.", "-..", "...", " ", "--", ".", " ", ".", "--", ".-", "..", ".-..",
      "...", ".-.-.-"])
])
def test_prepare_morse_code_to_convert(morse_code, expected):
    assert prepare_morse_code_to_convert(morse_code) == expected


@pytest.mark.parametrize('prepared_morse_code, expected', [
    ([".--.", "-.--", "-...", "..", "-", ".", "...", " ", "..", "...", " ", ".-", "--", ".-", "--..", "..", "-.", "--.",
      "-.-.--"], "pybites is amazing!"),
    (["-...", "---", "-...", " ", "...", ".", "-.", "-..", "...", " ", "--", ".", " ", ".", "--", ".-", "..", ".-..",
      "...", ".-.-.-"], "bob sends me emails.",)
])
def test_convert_to_text(prepared_morse_code: list, expected: str):
    assert convert_to_text(prepared_morse_code) == expected
