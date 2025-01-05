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
    Checks if a given number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of cubes of its digits.

    Parameters:
        n: The number to check.

    Returns -> bool:
        True if n is an Armstrong number, False otherwise.

    Raises:
        AssertionError: If n is negative.
        AssertionError: If n is not an integer.

    Examples:
        >>> is_armstrong_number(153)
        True  # 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
        >>> is_armstrong_number(370)
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

    # Determine if the number is an Armstrong number
    # by summing the cubes of its digits.
    # and comparing it to the original number.
    temp = n
    sum_of_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit**3
        temp //= 10

    return sum_of_cubes == n
