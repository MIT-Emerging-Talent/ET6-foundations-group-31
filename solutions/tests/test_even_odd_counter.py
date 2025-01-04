import unittest
from ..even_odd_counter import count_even_odd


class TestCountEvenOdd(unittest.TestCase):
    """Unit tests for the `count_even_odd` function."""

    def test_mixed_list(self):
        """Test with a list of mixed even and odd numbers."""
        self.assertEqual(count_even_odd([1, 2, 3, 4]), {"even": 2, "odd": 2})

    def test_all_even(self):
        """Test with a list of all even numbers."""
        self.assertEqual(count_even_odd([2, 4, 6, 8]), {"even": 4, "odd": 0})

    def test_all_odd(self):
        """Test with a list of all odd numbers."""
        self.assertEqual(count_even_odd([1, 3, 5, 7]), {"even": 0, "odd": 4})

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(count_even_odd([]), {"even": 0, "odd": 0})

    def test_invalid_input(self):
        """Test with invalid input containing non-integer elements."""
        with self.assertRaises(ValueError):
            count_even_odd([1, 2, "three", 4])


if __name__ == "__main__":
    unittest.main()
