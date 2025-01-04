"""
Unit Tests for Palindrome Checker

This module contains unit tests for the `palindrome_checker` function
defined in `palindrome_checker.py`. It validates correct behavior
for various input cases, including boundary and defensive checks.
"""

import unittest
from ..palindrome_checker import palindrome_checker


class TestPalindromeChecker(unittest.TestCase):
    """Unit tests for the `palindrome_checker` function."""

    def test_regular_palindrome(self):
        """Test a regular palindrome word."""
        self.assertTrue(palindrome_checker("madam"))

    def test_non_palindrome(self):
        """Test a word that is not a palindrome."""
        self.assertFalse(palindrome_checker("hello"))

    def test_palindrome_with_spaces(self):
        """Test a palindrome phrase containing spaces."""
        self.assertTrue(palindrome_checker("A man a plan a canal Panama"))

    def test_case_insensitivity(self):
        """Test a palindrome word with mixed case letters."""
        self.assertTrue(palindrome_checker("RaceCar"))

    def test_invalid_input(self):
        """Test with invalid input types (non-string)."""
        with self.assertRaises(TypeError):
            palindrome_checker(12345)  # Fixed indentation

    def test_empty_string(self):
        """Test with an empty string as input."""
        self.assertTrue(palindrome_checker(""))


if __name__ == "__main__":
    unittest.main()
