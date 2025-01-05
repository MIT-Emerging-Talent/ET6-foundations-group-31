"""
prime_checker

Description: This module provides a function to check if a given number is a prime number.
The function evaluates the number and returns "Prime" if it is a prime number, or "Not Prime".

Created on: 04/01/2025
# spell-checker: disable
@author: Thilakan Jegatheeswaran
# spell-checker: enable
"""


def prime_checker(number: int) -> str:
    """
    Checks if a given number is a prime number.

    Parameters:
        number (int): The number to check whether it is a prime number.

    Returns:
        str: "Prime" if the number is prime, "Not Prime" otherwise.

    Examples:
        >>> prime_checker(2)
        'Prime'
        >>> prime_checker(4)
        'Not Prime'
        >>> prime_checker(13)
        'Prime'
    """
    # Input validation: check if the number is an integer
    if not isinstance(number, int):
        raise ValueError("The input must be an integer.")

    # Numbers less than 2 are not prime
    if number < 2:
        return "Not Prime"

    # Check divisors from 2 up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "Not Prime"

    return "Prime"
