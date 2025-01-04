"""
Unit Tests for Anagram Checker

This module contains unit tests for the `anagram_checker` function
defined in `anagram_checker.py`. It validates the behavior for
various input cases, including boundary and defensive checks.
"""

import unittest
from ..anagram_checker import anagram_checker


class TestAnagramChecker(unittest.TestCase):
    """Unit tests for the `is_anagram` function."""

    def test_valid_anagram(self):
        """Test two strings that are valid anagrams."""
        self.assertTrue(anagram_checker("listen", "silent"))

    def test_invalid_anagram(self):
        """Test two strings that are not anagrams."""
        self.assertFalse(anagram_checker("hello", "world"))

    def test_anagram_with_spaces(self):
        """Test anagrams where strings contain spaces."""
        self.assertTrue(anagram_checker("triangle", "integral"))

    def test_case_insensitivity(self):
        """Test anagrams with different cases."""
        self.assertTrue(anagram_checker("Listen", "Silent"))

    def test_invalid_input_types(self):
        """Test handling of invalid input types."""
        with self.assertRaises(TypeError):
            anagram_checker(123, "abc")

    def test_empty_strings(self):
        """Test with empty strings."""
        self.assertTrue(anagram_checker("", ""))


if __name__ == "__main__":
    unittest.main()
