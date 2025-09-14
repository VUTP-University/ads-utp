"""
This module demonstrates various string indexing techniques in Python, including:
- string_indexing(str, index): Returns the character at the given index.
- string_slicing_step(str, start, end, step): Returns a substring with a specified step.
- string_concatenation(str1, str2): Concatenates two strings.
- string_reverse(str): Returns the reverse of the input string.
"""

def string_indexing(str, index):
    """
    Returns the character at the given index in the string.

    Args:
        str (str): The input string.
        index (int): The index of the character to retrieve.

    Returns:
        str: The character at the given index.
    """
    return str[index]


def string_slicing_step(str, start, end, step):
    """
    Returns a substring of the input string from the start index to the end index with a given step.

    Args:
        str (str): The input string.
        start (int): The start index of the substring.
        end (int): The end index of the substring.
        step (int): The step size for slicing.

    Returns:
        str: The substring from the start index to the end index with the given step.
    """
    return str[start:end:step]


def string_concatenation(str1, str2):
    """
    Returns the concatenation of two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenation of the two strings.
    """
    return str1 + str2


def string_reverse(str):
    """
    Returns the reverse of the input string.

    Args:
        str (str): The input string.

    Returns:
        str: The reverse of the input string.
    """
    return str[::-1]


# Example usage
print("At index 2:", string_indexing("Hello, World!", 2))  # Output: 'l'
print("Slicing with step 2:", string_slicing_step("Hello, World!", 0, 13, 2))  # Output: 'Hlo ol!'
print("Concatenation:", string_concatenation("Hello, ", "World!"))  # Output: 'Hello, World!'
print("Reversed string:", string_reverse("Hello, World!"))  # Output: '!dlroW ,olleH'