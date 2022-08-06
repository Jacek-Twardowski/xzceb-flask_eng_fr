import unittest
from translator import french_to_english, english_to_french

class TestTranslate(unittest.TestCase): 
    def testNull(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(english_to_french("None"), '')
    def testText(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(english_to_french("Hello"),"Bonjour") 

unittest.main()
