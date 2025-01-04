def is_palindrome(word):
    """
    Check if a given word is a palindrome.
    
    A palindrome is a word that reads the same forward and backward.
    
    Args:
        word (str): The word to check.
    
    Returns:
        bool: True if the word is a palindrome, False otherwise.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")
    cleaned_word = word.lower().replace(" ", "")
    return cleaned_word == cleaned_word[::-1]
