#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains unit tests for the `is_armstrong_number` function.

**Test Categories:**

* **Standard Cases:**
    - Tests with known Armstrong numbers (e.g., 153, 370).
    - Tests with known non-Armstrong numbers (e.g., 121, 100).

* **Edge Cases:**
    - Tests with zero (0).
    - Tests for extremely large numbers, their Armstrong property
    depends on the number of digits..

* **Defensive Tests:**
    - Tests with negative input values.
    - Tests with non-integer input values (e.g., floats, strings).

Created on 2025-01-04
Author: Muqadsa Tahir
"""

import unittest

from ..is_armstrong_number import is_armstrong_number


class TestIsArmstrongNumber(unittest.TestCase):
    """Unit tests for the is_armstrong_number function.

    Tests cover various scenarios, including:

    - Armstrong numbers
    - Non-Armstrong numbers
    - Negative input
    - Non-integer input
    - Edge cases
    """

    def test_armstrong_number_zero(self):
        """Tests for edge case 0"""
        self.assertTrue(is_armstrong_number(0))

    def test_armstrong_number_one(self):
        """Tests if 1 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(1))

    def test_armstrong_number_nine(self):
        """Tests if 9 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(9))

    def test_armstrong_number_153(self):
        """Tests if 153 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(153))

    def test_armstrong_number_370(self):
        """Tests if 370 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(370))

    def test_armstrong_number_371(self):
        """Tests if 371 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(371))

    def test_armstrong_number_407(self):
        """Tests if 407 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(407))

    def test_large_numbers_1634(self):
        """Tests if 1634 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(1634))

    def test_large_numbers_8208(self):
        """Tests if 8208 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(8208))

    def test_armstrong_number_93084(self):
        """Tests if 93084 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(93084))

    def test_armstrong_number_9926315(self):
        """Tests if 9926315 is an Armstrong number."""
        self.assertTrue(is_armstrong_number(9926315))

    def test_non_armstrong_number_121(self):
        """Tests if 121 is not an Armstrong number."""
        self.assertFalse(is_armstrong_number(121))

    def test_non_armstrong_number_100(self):
        """Tests if 100 is not an Armstrong number."""
        self.assertFalse(is_armstrong_number(100))

    def test_non_armstrong_number_123(self):
        """Tests if 123 is not an Armstrong number."""
        self.assertFalse(is_armstrong_number(123))

    def test_non_armstrong_number_18(self):
        """Tests if 18 is not an Armstrong number."""
        self.assertFalse(is_armstrong_number(18))

    def test_edge_case_10(self):
        """Tests if 2-digit 10 is not an Armstrong number."""
        self.assertFalse(is_armstrong_number(10))

    def test_edge_case_1000(self):
        """Tests if a 4-digit large n is not an Armstrong number."""
        self.assertFalse(is_armstrong_number(1000))

    def test_edge_case_10_digit(self):
        """Tests if a 10-digit large n is an Armstrong number."""
        self.assertTrue(is_armstrong_number(4679307774))

    def test_edge_case_39_digit(self):
        """Tests if a 39-digit large n is an Armstrong number."""
        self.assertTrue(is_armstrong_number(115132219018763992565095597973971522401))

    def test_negative_input(self):
        """Tests if TypeError is raised for negative input."""
        with self.assertRaises(AssertionError):
            is_armstrong_number(-1)

    def test_non_integer_input_float(self):
        """Tests if TypeError is raised for float input."""
        with self.assertRaises(TypeError):
            is_armstrong_number(3.14)

    def test_non_integer_input_string(self):
        """Tests if TypeError is raised for string input."""
        with self.assertRaises(TypeError):
            is_armstrong_number("123")

    def test_non_integer_empty_string(self):
        """Tests if TypeError is raised for empty string input."""
        with self.assertRaises(TypeError):
            is_armstrong_number("")

    def test_non_numeric_input(self):
        """Tests if TypeError is raised for non numeric character input."""
        with self.assertRaises(TypeError):
            is_armstrong_number("abc")


if __name__ == "__main__":
    unittest.main()
