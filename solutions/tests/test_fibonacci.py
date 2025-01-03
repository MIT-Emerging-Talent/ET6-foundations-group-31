""" "This is a test module for the fibonacci function."""


def fibonacci(n):
    # Ensure the input is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Generate Fibonacci sequence
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib


def test_fibonacci():
    # Valid input tests
    # Test for n=0, should return an empty list
    assert fibonacci(0) == []
    print("Test passed for n=0")

    # Test for n=1, should return [0]
    assert fibonacci(1) == [0]
    print("Test passed for n=1")

    # Test for n=5, should return [0, 1, 1, 2, 3]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    print("Test passed for n=5")

    # Test for n=10, should return the first 10 Fibonacci numbers
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print("Test passed for n=10")


# Run the tests
test_fibonacci()
