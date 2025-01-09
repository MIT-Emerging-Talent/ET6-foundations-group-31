"""
Unit tests for the `temperature_converter` functions.
This module tests the conversion of temperatures between Celsius and Fahrenheit.

Author: Safa Saber
"""

import unittest
from solutions.temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

class TestTemperatureConverter(unittest.TestCase):
    """Unit tests for the `temperature_converter` functions."""

    def test_celsius_to_fahrenheit_zero(self):
        """Test converting 0°C to Fahrenheit."""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_celsius_to_fahrenheit_hundred(self):
        """Test converting 100°C to Fahrenheit."""
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_celsius_to_fahrenheit_negative(self):
        """Test converting -40°C to Fahrenheit."""
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_fahrenheit_to_celsius_freezing(self):
        """Test converting 32°F to Celsius."""
        self.assertEqual(fahrenheit_to_celsius(32), 0.0)

    def test_fahrenheit_to_celsius_boiling(self):
        """Test converting 212°F to Celsius."""
        self.assertEqual(fahrenheit_to_celsius(212), 100.0)

    def test_fahrenheit_to_celsius_negative(self):
        """Test converting -40°F to Celsius."""
        self.assertEqual(fahrenheit_to_celsius(-40), -40.0)

    def test_invalid_celsius_input(self):
        """Test invalid input for Celsius to Fahrenheit conversion."""
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit("not a number")
        
    def test_invalid_fahrenheit_input(self):
        """Test invalid input for Fahrenheit to Celsius conversion."""
        with self.assertRaises(ValueError):
            fahrenheit_to_celsius("not a number")
        
if __name__ == "__main__":
    unittest.main()
