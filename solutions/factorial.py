def factorial(n):
    """
        Calculate the factorial of a number using recursion.

        Args:
            n (int): The number to calculate the factorial for.

        Returns:
            int: The factorial of the number.

        Raises:
            ValueError: If `n` is a negative integer.

        Examples:
            >>> factorial(5)
            120
            >>> factorial(0)
            1

    @author: Myat Charm
    Created on Jan 5, 2025.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
