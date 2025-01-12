"""
Test module for wallet_exchange function.

Created on: 10 Jan 2025
@author: MD Jubayer Khan
"""

import unittest
from solutions.wallet_exchange import wallet_exchange


class TestWalletExchange(unittest.TestCase):
    """
    Unit tests for the wallet_exchange function.
    """

    def test_even_difference(self):
        """It should return 'Bob' when the difference is even."""
        self.assertEqual(wallet_exchange(4, 2), "Bob")
        self.assertEqual(wallet_exchange(100, 98), "Bob")

    def test_odd_difference(self):
        """It should return 'Alice' when the difference is odd."""
        self.assertEqual(wallet_exchange(5, 4), "Alice")
        self.assertEqual(wallet_exchange(7, 2), "Alice")

    def test_large_numbers(self):
        """It should handle large numbers correctly."""
        self.assertEqual(wallet_exchange(1000001, 999996), "Alice")
        self.assertEqual(wallet_exchange(1000000, 999998), "Bob")

    def test_negative_numbers(self):
        """It should handle negative numbers correctly."""
        self.assertEqual(wallet_exchange(-5, -4), "Alice")
        self.assertEqual(wallet_exchange(-4, -2), "Bob")

    def test_zero_difference(self):
        """It should return 'Bob' when the difference is zero."""
        self.assertEqual(wallet_exchange(0, 0), "Bob")


if __name__ == "__main__":
    unittest.main()
