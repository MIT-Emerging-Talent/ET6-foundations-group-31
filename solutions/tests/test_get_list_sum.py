#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-01-03
@author: Muqadsa Tahir
"""

import unittest

# Import the 'patch' function for mocking objects during testing.
from unittest.mock import patch

from ..get_list_sum import get_list_sum


class TestGetListSum(unittest.TestCase):
    """Test the get_list_sum function"""

    def test_zero_sequence_length(self):
        """Tests that the sum is 0 for zero sequence length."""
        self.assertEqual(get_list_sum(0), 0)

    def test_negative_sequence_length(self):
        """Tests that an AssertionError is raised with negative sequence_length."""
        with self.assertRaises(AssertionError):
            get_list_sum(-1)

    def test_non_integer_sequence_length(self):
        """Tests that an AssertionError is raised with non-integer sequence_length."""
        with self.assertRaises(TypeError):
            get_list_sum("3")

    def test_very_large_sequence_length(self):
        """Tests with a very large sequence_length."""
        with patch("builtins.input", side_effect=["1"] * 100):  # Simulate 100 inputs
            self.assertEqual(get_list_sum(100), 100)

    def test_empty_list(self):
        """Tests with an empty input list."""
        with self.assertRaises(TypeError):
            get_list_sum([])

    def test_positive_numbers(self):
        """Tests with positive numbers as input."""
        with patch("builtins.input", side_effect=["1", "2", "3"]):
            self.assertEqual(get_list_sum(3), 6)

    def test_negative_numbers(self):
        """Tests with negative numbers as input."""
        with patch("builtins.input", side_effect=["-1", "0", 5]):
            self.assertEqual(get_list_sum(3), 4)

    def test_zeroes(self):
        """Tests with zero as input."""
        with patch("builtins.input", side_effect=["0", "0", "0"]):
            self.assertEqual(get_list_sum(3), 0)

    def test_large_numbers(self):
        """Tests with large numbers as input."""
        with patch("builtins.input", side_effect=["10", 20, 30]):
            self.assertEqual(get_list_sum(3), 60)

    def test_non_numeric_input(self):
        """Tests with non-numeric input."""
        with patch("builtins.input", side_effect=["1", "a", "3"]):
            with self.assertRaises(ValueError):
                get_list_sum(3)

    def test_single_positive_number(self):
        """Tests with a single positive number as input."""
        with patch("builtins.input", side_effect=["5"]):
            self.assertEqual(get_list_sum(1), 5)

    def test_single_negative_number(self):
        """Tests with a single negative number as input."""
        with patch("builtins.input", side_effect=["-2"]):
            self.assertEqual(get_list_sum(1), -2)
