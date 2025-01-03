import unittest
from ..string_permutations import find_permutations

class TestFindPermutations(unittest.TestCase):
    """Unit tests for the `find_permutations` function."""

    def test_regular_string(self):
        """Test with a standard string."""
        result = find_permutations("abc")
        expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        self.assertEqual(result, expected)

    def test_single_character(self):
        """Test with a single character."""
        result = find_permutations("a")
        self.assertEqual(result, ["a"])

    def test_empty_string(self):
        """Test with an empty string."""
        result = find_permutations("")
        self.assertEqual(result, [""])

    def test_repeating_characters(self):
        """Test with repeating characters."""
        result = find_permutations("aab")
        expected = ['aab', 'aba', 'baa']
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        """Test with invalid input."""
        with self.assertRaises(TypeError):
            find_permutations(123)

if __name__ == "__main__":
    unittest.main()
