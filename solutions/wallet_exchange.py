"""
Module: Wallet Exchange

Description: This module determines the winner based on the difference
between two integers. If the difference is even, the winner is "Bob";
if the difference is odd, the winner is "Alice".

Created on: 10 Jan 2025
@author: MD Jubayer Khan
"""


def wallet_exchange(a: int, b: int) -> str:
    """
    Determines the winner based on the difference between two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        str: "Bob" if the difference is even, "Alice" if the difference is odd.

    Raises:
        TypeError: If either input is not an integer.

    Examples:
        >>> wallet_exchange(4, 2)
        'Bob'
        >>> wallet_exchange(5, 3)
        'Alice'
        >>> wallet_exchange(1000001, 999997)
        'Alice'
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")

    # Compute the absolute difference
    difference = abs(a - b)

    # Return the correct result based on the parity of the difference
    return "Alice" if difference % 2 != 0 else "Bob"
