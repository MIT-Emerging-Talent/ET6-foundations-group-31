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
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)

    @staticmethod
    def reverse_text(text: str) -> str:
        return text[::-1]

    @staticmethod
    def to_uppercase(text: str) -> str:
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

    # Log the results for visibility
    logging.debug(f"Vowel Count Test Results: {results['Vowel Count Test Results']}")
    logging.debug(f"Reverse Text Test Results: {results['Reverse Text Test Results']}")
    logging.debug(
        f"Uppercase Conversion Test Results: {results['Uppercase Conversion Test Results']}"
    )

    return results


# Run the tests and log the results
run_tests()
