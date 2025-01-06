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

from ..mean_and_median import mean_and_median


class TestMeanAndMedian(unittest.TestCase):
    """Unit tests for the function `mean_and_median`."""

    def test_regular_list(self):
        """Test with a standard list containing multiple numbers."""
        self.assertEqual(mean_and_median([1, 2, 3, 4, 5]), (3.0, 3))
        self.assertEqual(mean_and_median([1, 2, 3, 4, 5, 6]), (3.5, 3.5))

    def test_empty_list(self):
        """Test case for an empty input list."""
        self.assertEqual(mean_and_median([]), (None, None))

    def test_single_element_list(self):
        """Test case with a single element in the list."""
        self.assertEqual(mean_and_median([42]), (42.0, 42))

    def test_unsorted_list(self):
        """Test case with an unsorted list."""
        self.assertEqual(
            mean_and_median([3, 1, 4, 1, 5, 9, 2]), (3.5714285714285716, 3)
        )

    def test_invalid_input(self):
        """Test case for invalid input (non-list types)."""
        with self.assertRaises(TypeError):
            mean_and_median("not a list")
        with self.assertRaises(TypeError):
            mean_and_median(123)
        with self.assertRaises(TypeError):
            mean_and_median(None)


if __name__ == "__main__":
    unittest.main()
