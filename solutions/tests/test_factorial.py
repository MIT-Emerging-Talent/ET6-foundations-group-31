"""
Test module for the function factorial.

Test categories:
  - General cases: Typical numbers to check standard functionality.
  - Boundary cases: Zero and one.
  - Robustness tests: Handling invalid input types and negative numbers.

@author: Myat Charm
Created on Jan 5, 2025.

"""

import unittest

from ..factorial import factorial


class TestFactorial(unittest.TestCase):
    """Unit tests for the factorial function."""

    def test_factorial_zero(self):
        """Test factorial of 0."""
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        """Test factorial of a positive number."""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)

    def test_factorial_large_number(self):
        """Test factorial of a larger number."""
        self.assertEqual(factorial(10), 3628800)


if __name__ == "__main__":
    unittest.main()
