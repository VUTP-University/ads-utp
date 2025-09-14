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
print("Transform String to Uppercase:", transform_string_upper("Hello, World!"))  # Output: 'HELLO, WORLD!'
print("Transform String to Lowercase:", transform_string_lower("Hello, World!"))  # Output: 'hello, world!'
print("Capitalize String:", transform_string_capitalize("hello, world!"))  # Output: 'Hello, world!'
print("Title Case String:", transform_string_title("hello, world!"))  # Output: 'Hello, World!'
print("Replace 'World' with 'Python':", string_replace("Hello, World!", "World", "Python"))  # Output: 'Hello, Python!'