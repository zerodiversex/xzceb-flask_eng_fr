import unittest
from translator import english_to_french, french_to_english

class TestTranslationModule(unittest.TestCase):

    def test_englishToFrench_assertNotEqual(self):
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour1')

    def test_englishToFrench_assertEqual(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchToEnglish_assertNotEqual(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello1')

    def test_frenchToEnglish_assertEqual(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()