"""This module is prime_checker."""
# test_prime.py
def is_prime(n):
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Edge cases
    if n <= 1:
        return False  # 1 and numbers less than 1 are not prime
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to the square root of n
        if n % i == 0:
            return False  # If divisible by any number, it's not prime
    return True  # If no divisors were found, n is prime
