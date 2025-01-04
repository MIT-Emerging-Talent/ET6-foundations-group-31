import logging

"""
test_text_processor

Description: This module tests the functions in the text_processor module, including counting vowels, reversing text, and converting text to uppercase.

Created on: 04/01/2025
# spell-checker: disable
@author: Thilakan Jegatheeswaran
# spell-checker: enable
"""

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class TextProcessor:
    """
    A class to encapsulate text processing functions such as counting vowels,
    reversing text, and converting text to uppercase.
    """

    @staticmethod
    def count_vowels(text: str) -> int:
        # Defensive assertion to ensure the input is a string
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)

    @staticmethod
    def reverse_text(text: str) -> str:
        # Defensive assertion to ensure the input is a string
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        return text[::-1]

    @staticmethod
    def to_uppercase(text: str) -> str:
        # Defensive assertion to ensure the input is a string
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        return text.upper()


def test_count_vowels():
    processor = TextProcessor()
    results = [
        processor.count_vowels("hello"),  # Expected: 2
        processor.count_vowels("HELLO"),  # Expected: 2
        processor.count_vowels("Python"),  # Expected: 1
        processor.count_vowels("aeiou"),  # Expected: 5
        processor.count_vowels("bcdfg"),  # Expected: 0
        processor.count_vowels("Aeiou"),  # Expected: 5 (case-insensitive)
        processor.count_vowels(""),  # Expected: 0 (empty string)
    ]

    # Adding assertions to validate results
    assert results == [
        2,
        2,
        1,
        5,
        0,
        5,
        0,
    ], f"Expected [2, 2, 1, 5, 0, 5, 0], but got {results}"
    return results


def test_reverse_text():
    processor = TextProcessor()
    results = [
        processor.reverse_text("hello"),  # Expected: "olleh"
        processor.reverse_text("Python"),  # Expected: "nohtyP"
        processor.reverse_text("12345"),  # Expected: "54321"
        processor.reverse_text(""),  # Expected: ""
        processor.reverse_text("  "),  # Expected: "  " (whitespace)
        processor.reverse_text("A!B@C#"),  # Expected: "#C@B!A" (special characters)
    ]

    # Adding assertions to validate results
    assert results == [
        "olleh",
        "nohtyP",
        "54321",
        "",
        "  ",
        "#C@B!A",
    ], f"Expected ['olleh', 'nohtyP', '54321', '', '  ', '#C@B!A], but got {results}"
    return results


def test_to_uppercase():
    processor = TextProcessor()
    results = [
        processor.to_uppercase("hello"),  # Expected: "HELLO"
        processor.to_uppercase("Python"),  # Expected: "PYTHON"
        processor.to_uppercase("12345"),  # Expected: "12345"
        processor.to_uppercase("!@#$"),  # Expected: "!@#$"
        processor.to_uppercase("aEiOu"),  # Expected: "AEIOU" (case-insensitive)
        processor.to_uppercase(" "),  # Expected: " " (whitespace)
    ]

    # Adding assertions to validate results
    assert results == [
        "HELLO",
        "PYTHON",
        "12345",
        "!@#$",
        "AEIOU",
        " ",
    ], f"Expected ['HELLO', 'PYTHON', '12345', '!@#$', 'AEIOU', ' '], but got {results}"
    return results


# Add tests for non-string inputs and boundary cases


def test_non_string_inputs():
    processor = TextProcessor()

    # Testing invalid non-string inputs
    invalid_inputs = [123, [1, 2, 3], None, 3.14, {"key": "value"}]

    for input_value in invalid_inputs:
        try:
            processor.count_vowels(input_value)
        except TypeError as e:
            logging.debug(f"TypeError for count_vowels with {input_value}: {e}")

        try:
            processor.reverse_text(input_value)
        except TypeError as e:
            logging.debug(f"TypeError for reverse_text with {input_value}: {e}")

        try:
            processor.to_uppercase(input_value)
        except TypeError as e:
            logging.debug(f"TypeError for to_uppercase with {input_value}: {e}")


def test_boundary_cases():
    processor = TextProcessor()

    # Test for very long strings (1 million characters)
    long_string = "a" * 10**6
    assert (
        processor.count_vowels(long_string) == 10**6
    )  # All vowels, so count should be 1 million
    assert (
        processor.reverse_text(long_string) == long_string
    )  # The reverse of a long string of 'a's is the same
    assert (
        processor.to_uppercase(long_string) == "A" * 10**6
    )  # All 'a's should become 'A's

    # Test for special characters
    special_string = "hello! How are you?"
    assert processor.count_vowels(special_string) == 7  # Expected vowels count
    assert processor.reverse_text(special_string) == "?uoy era woH !olleh"
    assert processor.to_uppercase(special_string) == "HELLO! HOW ARE YOU?"

    # Test for very short strings
    assert processor.count_vowels("a") == 1  # One vowel
    assert processor.reverse_text("a") == "a"  # Single character reverse is same
    assert processor.to_uppercase("a") == "A"  # Uppercase conversion

    assert processor.count_vowels("") == 0  # Empty string
    assert processor.reverse_text("") == ""  # Empty string
    assert processor.to_uppercase("") == ""  # Empty string


def run_tests():
    """
    Runs all the test functions and returns the results.

    Returns:
        dict: A dictionary with the test results.
    """
    results = {
        "Vowel Count Test Results": test_count_vowels(),
        "Reverse Text Test Results": test_reverse_text(),
        "Uppercase Conversion Test Results": test_to_uppercase(),
    }

    # Run additional tests
    test_non_string_inputs()
    test_boundary_cases()

    # Log the results for visibility
    logging.debug(f"Vowel Count Test Results: {results['Vowel Count Test Results']}")
    logging.debug(f"Reverse Text Test Results: {results['Reverse Text Test Results']}")
    logging.debug(
        f"Uppercase Conversion Test Results: {results['Uppercase Conversion Test Results']}"
    )

    return results


# Run the tests and log the results
run_tests()
