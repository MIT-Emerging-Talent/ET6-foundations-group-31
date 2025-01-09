"""
Module: temperature_converter
This module contains functions to convert temperatures between Celsius and Fahrenheit.
It includes two functions: one for converting Celsius to Fahrenheit, and the other
for converting Fahrenheit to Celsius.

@author: Safa Saber
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius to be converted.

    Returns:
        float: The temperature in Fahrenheit.

    Raises:
        ValueError: If the input is not a number.

    Doctests:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(-40)
        -40.0
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit to be converted.

    Returns:
        float: The temperature in Celsius.

    Raises:
        ValueError: If the input is not a number.

    Doctests:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
        >>> fahrenheit_to_celsius(-40)
        -40.0
    """
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    
    return (fahrenheit - 32) * 5 / 9
