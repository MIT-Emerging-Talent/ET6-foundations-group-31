import unittest
from ..palindrome_checker import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    """Unit tests for the `is_palindrome` function."""

    def test_regular_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_palindrome(12345)

if __name__ == "__main__":
    unittest.main()
