def count_even_odd(numbers):
    """
    Counts the number of even and odd numbers in a list.

    Parameters:
        numbers (list): A list of integers.

    Returns:
        dict: A dictionary with keys 'even' and 'odd' representing their respective counts.

    Example:
        >>> count_even_odd([1, 2, 3, 4])
        {'even': 2, 'odd': 2}
    """
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers")

    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count

    return {"even": even_count, "odd": odd_count}
