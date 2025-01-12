"""Calculate the Greatest Common Divisor (GCD) of two numbers
using the Euclidean algorithm.
"""


def gcd(a: int, b: int) -> int:
    """
    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of the two numbers.

    Examples:
        >>> gcd(15,5)
        5
        >>> gcd(18,63)
        9

    @author: Myat Charm
    Created on Jan 03, 2025.
    """
    assert isinstance(a, int) and isinstance(b, int), "Both inputs must be integers."

    while b != 0:
        a, b = b, a % b
    return a
