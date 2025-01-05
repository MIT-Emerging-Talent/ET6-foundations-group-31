"""
Test module for the prime_checker function.

Created on: 04/01/2025
@author: Thilakan Jegatheeswaran
"""

import unittest


# Directly define the prime_checker function inside the test file
def prime_checker(number: int) -> str:
    """
    Checks if a given number is a prime number.

    Parameters:
        number (int): The number to check whether it is a prime number.

    Returns:
        str: "Prime" if the number is prime, "Not Prime" otherwise.
    """
    if number < 2:
        return "Not Prime"
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"


class TestPrimeChecker(unittest.TestCase):
    """
    Unit tests for the prime_checker function.
    """

    def test_prime_number(self):
        """It should return 'Prime' for prime numbers."""
        self.assertEqual(prime_checker(2), "Prime")
        self.assertEqual(prime_checker(13), "Prime")
        self.assertEqual(prime_checker(17), "Prime")
        self.assertEqual(prime_checker(19), "Prime")

    def test_not_prime_number(self):
        """It should return 'Not Prime' for non-prime numbers."""
        self.assertEqual(prime_checker(4), "Not Prime")
        self.assertEqual(prime_checker(20), "Not Prime")
        self.assertEqual(prime_checker(1), "Not Prime")

    def test_negative_number(self):
        """It should return 'Not Prime' for negative numbers."""
        self.assertEqual(prime_checker(-5), "Not Prime")
        self.assertEqual(prime_checker(-2), "Not Prime")

    def test_zero(self):
        """It should return 'Not Prime' for zero."""
        self.assertEqual(prime_checker(0), "Not Prime")

    def test_large_prime(self):
        """It should handle large prime numbers."""
        self.assertEqual(prime_checker(101), "Prime")

    def test_large_not_prime(self):
        """It should handle large non-prime numbers."""
        self.assertEqual(prime_checker(100), "Not Prime")


if __name__ == "__main__":
    unittest.main()
