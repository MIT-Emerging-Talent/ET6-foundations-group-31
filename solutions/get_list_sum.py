#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the sum of numbers provided by the user.

Module contents:
    - get_list_sum: calculates the sum of numbers provided by the user.

Created on 2025-01-03
@author: Muqadsa Tahir
"""


def get_list_sum(sequence_length: int) -> int:
    """
    Calculates the sum of a list of numbers provided by the user.

    Parameters:
        sequence_length: The number of elements to be entered by the user.
            Must be a non-negative integer.

    Returns -> int:
        The sum of the numbers entered by the user.

    Raises:
            TypeError: If argument is not an integer.
            AssertionError: If argument is negative.

    Examples:
        >>> get_list_sum(7)  # Example (assuming user inputs: 1, 2, -5, 10 , -20 , 30, 5)
        23
        >>> get_list_sum(3)  # Example (assuming user inputs: 2, -5, 10)
        7
        >>> get_list_sum(4)  # Example (assuming user inputs: 1, 2, 3, 4)
        10
    """
    # the number should be an integer greater than 0
    assert sequence_length >= 0, "sequence_length must be non-negative"
    if not isinstance(sequence_length, int):
        raise TypeError("sequence_length must be an integer")

    if sequence_length == 0:
        return 0  # Handle zero sequence_length

    # This function first iteratively prompts the user to enter each number in the sequence.
    # Finally, it calculates and returns the sum of the entered numbers.

    numbers = []
    for i in range(sequence_length):
        try:
            number = int(input(f"Enter element {i+1}: "))
        except ValueError as exc:
            raise ValueError("Invalid input. Please enter a number.") from exc
        numbers.append(number)

    return sum(numbers)
