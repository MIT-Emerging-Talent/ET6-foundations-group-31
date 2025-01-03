"""This module runs the test for prime_checker."""


def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Test cases
print(is_prime(7))  # True
print(is_prime(4))  # False
print(is_prime(17))  # True
print(is_prime(20))  # False
