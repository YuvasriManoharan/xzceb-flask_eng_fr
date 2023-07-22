import unittest
import translator


class TestTranslator(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        

    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        

if __name__ == '__main__':
    unittest.main()