# -*- coding: utf-8 -*-
'''
Unit tests
'''
import unittest

from morsecodelib import text
from morsecodelib import alphabet


class TestText(unittest.TestCase):
    """
    Test text <--> code conversion
    """

    def setUp(self):
        self.message_text = 'testing text to code converSION!'
        self.message_code = ('- . ... - .. -. --.  - . -..- -  - ---  '
                             '-.-. --- -.. .  -.-. --- -. ...- . .-. ... .. --- -. -.-.--')

    def test_text_to_code(self):
        result = text.text_to_code(self.message_text)
        self.assertEqual(result, self.message_code)

    def test_code_to_text(self):
        result = text.code_to_text(self.message_code)
        self.assertEqual(result, self.message_text.upper())

    def test_sanity(self):
        """
        make sure it's compatible with itself
        """
        code1 = text.text_to_code(self.message_text)
        text1 = text.code_to_text(code1)
        code2 = text.text_to_code(text1)
        self.assertEqual(text1, self.message_text.upper())
        self.assertEqual(code1, code2)

    def test_extended_letters(self):
        self.assertIn(u'\u0635', alphabet.letters_to_code.keys())
        char1 = 'ه'
        char2 = 'س'
        # note that this script is printed right to left.
        self.assertEqual(text.text_to_code(
            char1 + char2), text.text_to_code('ES'))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
