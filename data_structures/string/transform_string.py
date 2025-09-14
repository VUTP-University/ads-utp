"""
This module provides functions to transform strings in various ways, such as converting to uppercase, 
lowercase, capitalizing, title casing, and replacing substrings.
- transform_string_upper(str): Converts all characters in the string to uppercase.
- transform_string_lower(str): Converts all characters in the string to lowercase.
- transform_string_capitalize(str): Capitalizes the first character of the string.
- transform_string_title(str): Converts the string to title case.
- string_replace(str, old, new): Replaces all occurrences of 'old' substring with 'new' substring in the string.
"""


def transform_string_upper(str):
    """
    Returns the transformed version of the input string - all characters in uppercase.

    Args:
        str (str): The input string.

    Returns:
        str: The transformed version of the input string.
    """
    return str.upper()


def transform_string_lower(str):
    """
    Returns the transformed version of the input string - all characters in lowercase.

    Args:
        str (str): The input string.

    Returns:
        str: The transformed version of the input string.
    """
    return str.lower()


def transform_string_capitalize(str):
    """
    Returns the transformed version of the input string - the first character in uppercase.

    Args:
        str (str): The input string.

    Returns:
        str: The transformed version of the input string.
    """
    return str.capitalize()


def transform_string_title(str):
    """
    Returns the transformed version of the input string - all words in title case.

    Args:
        str (str): The input string.

    Returns:
        str: The transformed version of the input string.
    """
    return str.title()


def string_replace(str, old, new):
    """
    Returns the transformed version of the input string - all occurrences of old replaced with new.

    Args:
        str (str): The input string.
        old (str): The substring to be replaced.
        new (str): The substring to replace with.

    Returns:
        str: The transformed version of the input string.
    """
    return str.replace(old, new)


# Example usage
if __name__ == "__main__":
    sample_string = "hello world"
    print(transform_string_upper(sample_string))        # Output: "HELLO WORLD"
    print(transform_string_lower(sample_string))        # Output: "hello world"
    print(transform_string_capitalize(sample_string))   # Output: "Hello world"
    print(transform_string_title(sample_string))        # Output: "Hello World"
    print(string_replace(sample_string, "world", "there"))  # Output: "hello there"