#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the evaluate_temperature function.
Created on 2025-01-01

@author: Raneem Rami
"""

import unittest

from ..evaluate_temperature import evaluate_temperature


class TestEvaluateTemperature(unittest.TestCase):
    """Test cases for the evaluate_temperature function."""

    def test_safe_temperature(self):
        """It should evaluate 25 to 'Safe'"""
        self.assertEqual(evaluate_temperature(25), "Safe")

    def test_normal_temperature(self):
        """It should evaluate 35 to 'Normal'"""
        self.assertEqual(evaluate_temperature(35), "Normal")

    def test_warning_temperature(self):
        """It should evaluate 45 to 'Warning'"""
        self.assertEqual(evaluate_temperature(45), "Warning")

    def test_freezing_temperature(self):
        """It should evaluate -15 to 'Freezing'"""
        self.assertEqual(evaluate_temperature(-15), "Freezing")

    def test_not_an_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            evaluate_temperature(1.0)

    def test_less_than_0(self):
        """It should raise an assertion error if the argument is larger than 50"""
        with self.assertRaises(AssertionError):
            evaluate_temperature(51)


if __name__ == "__main__":
    # Run all the test cases
    unittest.main()
