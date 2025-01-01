""" "This is a test module for the fibonacci function."""
# test_fibonacci.py

import os
import sys

# Add the parent directory of fibonacci.py to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import the fibonacci module
import unittest

from fibonacci import fibonacci  # Import the fibonacci function


class TestFibonacci(unittest.TestCase):
    """Test cases for the fibonacci function."""

    def test_valid_inputs(self):
        """Test fibonacci function with valid inputs."""
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibonacci(4), [0, 1, 1, 2])

    def test_invalid_inputs(self):
        """Test fibonacci function with invalid inputs."""
        with self.assertRaises(ValueError):
            fibonacci(-1)  # Negative input

        with self.assertRaises(ValueError):
            fibonacci("a")  # String input

        with self.assertRaises(ValueError):
            fibonacci(3.5)  # Float input

        with self.assertRaises(ValueError):
            fibonacci([])  # List input


if __name__ == "__main__":
    unittest.main()
