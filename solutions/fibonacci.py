"""This module provides the Fibonacci function."""
from typing import List

def fibonacci(n: int) -> List[int]:
    """
    Generates the Fibonacci sequence up to n terms.

    Args:
    n (int): The number of terms to generate in the Fibonacci sequence.

    Returns:
    list: A list containing the first n terms of the Fibonacci sequence.

    Example:
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Ensure this block runs only when the script is executed directly.
if __name__ == "__main__":
    # Example usage
    print("Fibonacci sequence for 10 terms:", fibonacci(10))
