"""
Unit Tests for String Reversal

This module contains unit tests for the `string_reversal` function
defined in `string_reversal.py`. It validates correct behavior
for various input cases, including boundary and defensive checks.

@author: Safa Saber
"""

import unittest
from solutions.string_reversal import string_reversal


class TestStringReversal(unittest.TestCase):
    """Unit tests for the `string_reversal` function."""

    def test_regular_string(self):
        """Test reversing a regular string."""
        self.assertEqual(string_reversal("hello"), "olleh")

    def test_single_character(self):
        """Test reversing a single character string."""
        self.assertEqual(string_reversal("a"), "a")

    def test_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(string_reversal(""), "")

    def test_palindrome_string(self):
        """Test reversing a palindrome string."""
        self.assertEqual(string_reversal("madam"), "madam")

    def test_mixed_case_string(self):
        """Test reversing a string with mixed case."""
        self.assertEqual(string_reversal("Safa"), "afaS")

    def test_numeric_string(self):
        """Test reversing a numeric string."""
        self.assertEqual(string_reversal("12345"), "54321")

    def test_special_characters_string(self):
        """Test reversing a string with special characters."""
        self.assertEqual(string_reversal("!@#$%"), "%$#@!")

    def test_invalid_input(self):
        """Test with invalid input types (non-string)."""
        with self.assertRaises(ValueError):
            string_reversal(
                12345
            )  # Should raise ValueError because input is not a string


if __name__ == "__main__":
    unittest.main()
