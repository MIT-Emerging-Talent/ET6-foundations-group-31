"""
Unit tests for the `make_chocolate` function in the `make_chocolate` module.

These tests verify:
- Correct calculation of required small bars
- Defensive assertions for invalid inputs
- Boundary cases where the goal cannot be achieved

@author: May Mon Thant
"""

import sys
import unittest
from pathlib import Path

# Add the parent directory to the system path to import the solutions module
sys.path.append(str(Path(__file__).resolve().parents[2]))

from solutions.make_chocolate import make_chocolate  # noqa: E402


class TestMakeChocolate(unittest.TestCase):
    """Tests for the `make_chocolate` function."""

    def test_regular_case(self):
        """Test a typical case where the goal is achievable."""
        self.assertEqual(make_chocolate(4, 1, 9), 4)

    def test_exceeds_goal(self):
        """Test when the goal exceeds the total available bars."""
        self.assertEqual(make_chocolate(4, 1, 10), -1)

    def test_mix_of_bars(self):
        """Test a mix of big and small bars to meet the goal."""
        self.assertEqual(make_chocolate(4, 1, 7), 2)

    def test_goal_exact_with_big_bars(self):
        """Test when the goal is met using only big bars."""
        self.assertEqual(make_chocolate(0, 3, 15), 0)

    def test_goal_unachievable_with_big_bars(self):
        """Test when big bars alone cannot achieve the goal."""
        self.assertEqual(make_chocolate(4, 2, 14), 4)

    def test_goal_unachievable_no_small_bars(self):
        """Test when no small bars are available to meet the goal."""
        self.assertEqual(make_chocolate(0, 2, 11), -1)

    def test_invalid_negative_input(self):
        """Test that negative inputs raise a ValueError."""
        with self.assertRaises(ValueError):
            make_chocolate(-1, 2, 9)

    def test_zero_goal(self):
        """Test when the goal is zero, requiring no bars."""
        self.assertEqual(make_chocolate(4, 2, 0), 0)

    def test_boundary_case(self):
        """Test when the goal equals the exact number of available bars."""
        self.assertEqual(make_chocolate(3, 2, 13), 3)


if __name__ == "__main__":
    unittest.main()
