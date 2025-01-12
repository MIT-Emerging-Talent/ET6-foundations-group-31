"""
Test module for the word_comparator function.

Created on: 03 01 25
@author: MD Jubayer Khan
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from word_comparator import word_comparator


class TestWordComparator(unittest.TestCase):
    """
    Unit tests for the word_comparator function.
    """

    # Tests for valid word comparisons
    def test_same_words_basic(self):
        """It should return True for words with the same sorted characters."""
        self.assertTrue(word_comparator("listen", "silent"))

    def test_same_words_scrambled(self):
        """It should return True for words with scrambled same characters."""
        self.assertTrue(word_comparator("word", "wrdo"))

    def test_different_words_basic(self):
        """It should return False for words with different characters."""
        self.assertFalse(word_comparator("hello", "world"))

    def test_different_words_partial_match(self):
        """It should return False for words with partially overlapping characters."""
        self.assertFalse(word_comparator("python", "pytho"))

    # Tests for edge cases
    def test_empty_strings(self):
        """It should return True for two empty strings."""
        self.assertTrue(word_comparator("", ""))

    def test_single_character_same(self):
        """It should return True for single-character words that are the same."""
        self.assertTrue(word_comparator("a", "a"))

    def test_single_character_different(self):
        """It should return False for single-character words that are different."""
        self.assertFalse(word_comparator("a", "b"))

    def test_special_characters_same(self):
        """It should return True for words with the same special characters."""
        self.assertTrue(word_comparator("!@#", "#@!"))

    def test_special_characters_different(self):
        """It should return False for words with different special characters."""
        self.assertFalse(word_comparator("!@#", "##@"))

    def test_whitespace_handling(self):
        """It should consider whitespace while comparing."""
        self.assertFalse(word_comparator("word", "word "))

    def test_long_strings_same(self):
        """It should return True for very long strings with the same characters."""
        word1 = "a" * 1000 + "b" * 1000
        word2 = "b" * 1000 + "a" * 1000
        self.assertTrue(word_comparator(word1, word2))

    def test_long_strings_different(self):
        """It should return False for very long strings with different characters."""
        word1 = "a" * 1000 + "b" * 1000
        word2 = "a" * 1000 + "c" * 1000
        self.assertFalse(word_comparator(word1, word2))

    # Defensive tests for invalid inputs
    def test_non_string_input_numbers(self):
        """It should raise a TypeError for non-string inputs like numbers."""
        with self.assertRaises(TypeError):
            word_comparator(123, 321)

    def test_non_string_input_mixed(self):
        """It should raise a TypeError for mixed valid and invalid inputs."""
        with self.assertRaises(TypeError):
            word_comparator("word", None)

    def test_non_string_input_lists(self):
        """It should raise a TypeError for list inputs."""
        with self.assertRaises(TypeError):
            word_comparator(["word"], ["drow"])


if __name__ == "__main__":
    unittest.main()
