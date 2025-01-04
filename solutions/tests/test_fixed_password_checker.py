"""
Test module for the fixed_password_checker function.

Created on: 03 01 25
@author: MD Jubayer Khan

"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fixed_password_checker import password_checker


class Test_fixed_password(unittest.TestCase):
    """
    Unit tests for the password_checker function.
    """

    def test_correct_password(self):
        """It should return 'Correct' when the password is correct."""
        self.assertEqual(password_checker(1999), "Correct")

    def test_wrong_password(self):
        """It should return 'Wrong' when the password is incorrect."""
        self.assertEqual(password_checker(1234), "Wrong")

    def test_negative_password(self):
        """It should handle negative numbers as invalid attempts."""
        self.assertEqual(password_checker(-1999), "Wrong")

    def test_large_number_password(self):
        """It should handle large numbers as invalid attempts."""
        self.assertEqual(password_checker(99999), "Wrong")

    def test_edge_case_zero(self):
        """It should return 'Wrong' for zero as an attempt."""
        self.assertEqual(password_checker(0), "Wrong")


if __name__ == "__main__":
    unittest.main()
