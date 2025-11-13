import unittest
from helpers import clean_string, remove_special_characters

class TestHelpers(unittest.TestCase):
    def test_clean_string(self):
        self.assertEqual(clean_string(" Hello World "), "helloworld")

    def test_remove_special_characters(self):
        self.assertEqual(remove_special_characters("he!!o@#"), "heo")

if __name__ == "__main__":
    unittest.main()
# test_helpers.py   