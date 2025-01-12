#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a given number is an Armstrong number.

Module contents:
    - is_armstrong_number: Checks if a given number is an Armstrong number.

Created on 2025-01-04
Author: Muqadsa Tahir
"""


def is_armstrong_number(n: int) -> bool:
    """
    Checks if a given number is an Armstrong number of first kind.

    An Armstrong number is a number where the sum of each digit raised to the power
    of the number of digits in that number is equal to the original number itself.

    Parameters:
        n: The number to check.

    Returns -> bool:
        True if n is an Armstrong number, False otherwise.

    Raises:
        AssertionError: If 'n' is negative.
        TypeError: If 'n' is not an integer.

    Examples:
        >>> is_armstrong_number(153)
        True  # 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
        >>> is_armstrong_number(4679307774)
        True
        >>> is_armstrong_number(121)
        False
        >>> is_armstrong_number(100)
        False
    """
    # the number should be an integer greater than 0
    assert n >= 0, "n must be non-negative"
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    # Determine the number of digits in the number.
    # Iterate through each digit in the string.
    # Calculate the power of the digit.
    # Add the power to the sum.
    number_string = str(n)
    number_of_digits = len(number_string)
    sum_of_powers = 0
    for digit in number_string:
        digit_int = int(digit)
        digit_power = digit_int**number_of_digits
        sum_of_powers += digit_power

    # Compare the sum of powers is to the original number
    return sum_of_powers == n
