"""
Test module for the longest_zero_substring function.

Created on: 12-01-2025
@author: MD Jubayer Khan
"""

import unittest
from solutions.longest_zero_substring import longest_zero_substring


class TestLongestZeroSubstring(unittest.TestCase):
    """
    Unit tests for the longest_zero_substring function.
    """

    def test_regular_case(self):
        """It should return the correct length for a typical case."""
        self.assertEqual(longest_zero_substring("1100100"), 2)

    def test_no_zeros(self):
        """It should return 0 when there are no zeros."""
        self.assertEqual(longest_zero_substring("111"), 0)

    def test_only_zeros(self):
        """It should return the length of the string when all are zeros."""
        self.assertEqual(longest_zero_substring("00000"), 5)

    def test_mixed_case(self):
        """It should correctly handle a mix of zeros and ones."""
        self.assertEqual(longest_zero_substring("001010001"), 3)

    def test_empty_string(self):
        """It should return 0 for an empty string."""
        self.assertEqual(longest_zero_substring(""), 0)

    def test_invalid_characters(self):
        """It should raise a ValueError for invalid characters."""
        with self.assertRaises(ValueError):
            longest_zero_substring("1012")

    def test_non_string_input(self):
        """It should raise a TypeError for non-string input."""
        with self.assertRaises(TypeError):
            longest_zero_substring(101)


if __name__ == "__main__":
    unittest.main()
