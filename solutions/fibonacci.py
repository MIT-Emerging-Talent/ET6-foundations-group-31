# fibonacci.py
from prime_checker import is_prime

def fibonacci(n):
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
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
print(fibonacci(10))  # Print the first 10 Fibonacci numbers
print(is_prime(fibonacci(10)[-1]))  # Check if the last Fibonacci number is prime
