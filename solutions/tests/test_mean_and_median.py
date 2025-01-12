"""
Test module for the function mean_and_median.

Test categories:
  - General cases: A set of typical lists to check standard functionality.
  - Boundary cases: Empty list, single element list.
  - Robustness tests: Handling invalid input types and assertion errors.

@author: Myat Charm
Created on Dec 27, 2024.

"""

import unittest

from solutions.mean_and_median import mean_and_median


class TestMeanAndMedian(unittest.TestCase):
    """Unit tests for the function `mean_and_median`."""

    def test_regular_list(self):
        """Test with a standard list containing multiple numbers."""
        self.assertEqual(mean_and_median([1, 2, 3, 4, 5]), (3.0, 3))
        self.assertEqual(mean_and_median([1, 3, 3, 6, 7, 8, 9]), (5.285714285714286, 6))

    def test_single_element_list(self):
        """Test with a list containing a single number."""
        self.assertEqual(mean_and_median([5]), (5.0, 5))

    def test_empty_list(self):
        """Test with an empty list, should raise ValueError."""
        with self.assertRaises(ValueError):
            mean_and_median([])

    def test_non_list_input(self):
        """Test with a non-list input, should raise TypeError."""
        with self.assertRaises(TypeError):
            mean_and_median("not a list")

    def test_non_numeric_elements(self):
        """Test with a list containing non-numeric elements, should raise TypeError."""
        with self.assertRaises(TypeError):
            mean_and_median([1, 2, "three", 4])

    def test_even_number_of_elements(self):
        """Test with a list containing an even number of elements."""
        self.assertEqual(mean_and_median([1, 2, 3, 4]), (2.5, 2.5))

    def test_odd_number_of_elements(self):
        """Test with a list containing an odd number of elements."""
        self.assertEqual(mean_and_median([1, 2, 3]), (2.0, 2))


if __name__ == "__main__":
    unittest.main()
