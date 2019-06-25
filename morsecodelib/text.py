# -*- coding: utf-8 -*-
"""
Convert Morse code <--> text
"""

from morsecodelib import alphabet


def text_to_code(text):
    """
    Convert text to Morse code symbols.

    If an invalid character is encountered, it is rendered as a question mark.

    Parameters
    ----------
    text : str
        text to convert to Morse code.

    Examples
    --------
    >>> text_to_code('hi')
    '.... ..'
    """
    code = []
    for word in text.split():
        morse_word = []
        for character in word:
            morse_word.append(alphabet.letters_to_code.get(character.upper(),
                                                           alphabet.letters_to_code['?']))
        code.append(' '.join(morse_word))
    return '  '.join(code)


def code_to_text(code):
    """
    Convert Morse code to text.

    Double spaces are considered gaps between words

    Parameters
    ----------
    code : str
        Morse code string to convert to text

    Examples
    --------
    >>> text_to_code('.... ..')
    'hi'
    """

    text = []
    for morse_word in code.split('  '):
        word = []
        for morse_sequence in morse_word.split(' '):
            letter = alphabet.code_to_letters.get(morse_sequence, '&')
            word.append(letter)
        text.append(''.join(word))
    return ' '.join(text)
