#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for evaluating the safety level of a temperature

Module content:
    -evaluate_temperature: evaluating the safety level of a temperature
created on 2025-01-01
@author: Raneem Rami
"""


def evaluate_temperature(celsius: int) -> str:
    """
    Evaluates the safety level of a temperature given in Celsius.

    Parameters:
        celsius: int, The temperature in Celsius to evaluate, (number must not be greater than 50).

    Returns ->  str:
        A string indicating the safety level of the temperature.

    Raises:
        AssertionError: if the argument is nor an integer
        AssertionError: if the argument is greater than 50

    Example:
    >>> evaluate_temperature(25)
    'Safe'

    >>> evaluate_temperature(35)
    'Normal'

    >>> evaluate_temperature(45)
    'Warning'

    >>> evaluate_temperature(-15)
    'Freezing'

    Notes:
    - Temperatures below -10°C and above 50°C are considered dangerous.
    """

    assert isinstance(celsius, int), "celsius is not an integer"
    assert celsius <= 50, "celsius is greater than 50"

    if celsius < -10:  # temperatures less than -10 are considered freezing.
        return "Freezing"

    if -10 <= celsius <= 30:  # temperatures from -10 to 30 are considered safe.
        return "Safe"

    if 31 <= celsius <= 40:  # temperatures from 31 to 40 are considered normal.
        return "Normal"

    if 41 <= celsius <= 50:  # temperatures from 41 to 50 are not safe (warning).
        return "Warning"
