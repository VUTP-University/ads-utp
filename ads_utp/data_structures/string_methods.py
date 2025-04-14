def string_length(s):
    """Return the length of the string.

    Args:
        s (string): The string to be measured.

    Returns:
        int: The length of the string.
    """
    return len(s)


def string_concat(s1, s2):
    """Concatenate two strings.

    Args:
        s1 (string): The first string.
        s2 (string): The second string.

    Returns:
        string: The concatenated string.
    """
    return s1 + s2


def string_to_lower(s):
    """Convert a string to lowercase.

    Args:
        s (string): The string to be converted.

    Returns:
        string: The string in lowercase.
    """
    return s.lower()


def string_to_upper(s):
    """Convert a string to uppercase.

    Args:
        s (string): The string to be converted.

    Returns:
        string: The string in uppercase.
    """
    return s.upper()


def string_swap_case(s):
    """Swap the case of a string.

    Args:
        s (string): The string to be converted.

    Returns:
        string: The string with swapped case.
    """
    return s.swapcase()


def string_reverse(s):
    """Reverse a string.

    Args:
        s (string): The string to be reversed.

    Returns:
        string: The reversed string.
    """
    return s[::-1]


def string_strip(s):
    """Strip whitespace from the beginning and end of a string.

    Args:
        s (string): The string to be stripped.

    Returns:
        string: The stripped string.
    """
    return s.strip()


def string_replace(s, old, new):
    """Replace occurrences of a substring in a string.

    Args:
        s (string): The original string.
        old (string): The substring to be replaced.
        new (string): The substring to replace with.

    Returns:
        string: The modified string.
    """
    return s.replace(old, new)