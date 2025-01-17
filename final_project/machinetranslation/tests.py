import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

class TestEnglishToFrench(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

unittest.main()