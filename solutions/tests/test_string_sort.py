"""
Unit tests for the `string_sort` function in the `string_sort` module.

These tests cover:
- Normal functionality
- Defensive assertions for invalid inputs
- Boundary cases

@author: May Mon Thant
"""

from solutions.string_sort import string_sort
import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


# noqa: E402
class TestStringSort(unittest.TestCase):
    """Tests for the `string_sort` function."""

    def test_regular_case(self):
        """Test sorting a typical string."""
        self.assertEqual(string_sort("hello"), "ehllo")

    def test_upper_and_lower_case(self):
        """Test sorting a string with mixed case."""
        self.assertEqual(string_sort("Python"), "Phnoty")

    def test_numeric_string(self):
        """Test sorting a string containing numbers."""
        self.assertEqual(string_sort("12345"), "12345")

    def test_special_characters(self):
        """Test sorting a string with special characters."""
        self.assertEqual(string_sort("!@#$%"), "!#$%@")

    def test_empty_string(self):
        """Test sorting an empty string raises ValueError."""
        with self.assertRaises(ValueError):
            string_sort("")

    def test_non_string_input(self):
        """Test passing a non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            string_sort(123)

    def test_single_character(self):
        """Test sorting a single character string."""
        self.assertEqual(string_sort("a"), "a")

    def test_boundary_case_two_characters(self):
        """Test sorting a string with two characters."""
        self.assertEqual(string_sort("ba"), "ab")


if __name__ == "__main__":
    unittest.main()
