#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for my_grade function.
created on 2025-01-05

@author: Raneem Rami

"""

import unittest

from ..my_grade import my_grade


class TestMyGrade(unittest.TestCase):
    """test the my_grade function"""

    # Test for Excellent grade (A)
    def test_excellent(self):
        """It should evaluate 3.6 to "Excellent (A)" """
        self.assertEqual(my_grade(3.6), "Excellent (A)")

    # Test for Very Good grade (B+)
    def test_very_good(self):
        """It should evaluate 3.5 to "Very good (B+)" """
        self.assertEqual(my_grade(3.5), "Very Good (B+)")

    # Test for Good grade (B)
    def test_good(self):
        """It should evaluate 2.8 to "Good (B)" """
        self.assertEqual(my_grade(2.8), "Good (B)")

    # Test for Satisfactory grade (C)
    def test_satisfactory(self):
        """It should evaluate 2.7 to "satisfactory (C)" """
        self.assertEqual(my_grade(2.7), "Satisfactory (C)")

    # Test for Basic grade (D)
    def test_basic(self):
        """It should evaluate 1.9 to "Basic (D)" """
        self.assertEqual(my_grade(1.9), "Basic (D)")

    # Test for Fail grade (F)
    def test_fail(self):
        """It should evaluate 1.5 to "Fail (F)" """
        self.assertEqual(my_grade(1.5), "Fail (F)")

    def test_argument_is_not_float(self):
        """It should raise an assertion error if argument is not a float"""
        with self.assertRaises(AssertionError):
            my_grade(3)

    def test_argument_is_greater_than_4(self):
        """It raises an assertion error if argument is grater than 4.0"""
        with self.assertRaises(AssertionError):
            my_grade(4.1)


# Running the tests
if __name__ == "__main__":
    unittest.main()
