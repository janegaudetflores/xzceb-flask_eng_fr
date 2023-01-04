import unittest
from translator import french_to_english, english_to_french

class TestTranslator_f2e(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('None'), '')
        self.assertNotEqual(french_to_english(0), 0)


class TestTranslator_e2f(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'), '')
        self.assertNotEqual(english_to_french(0), 0)

unittest.main()
