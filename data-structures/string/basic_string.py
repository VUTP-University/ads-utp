def string_length(str):
    """
    Returns the length of the input string.

    Args:
        str (str): The input string.

    Returns:
        int: The length of the input string.
    """
    return len(str)

def substring_count(str, substr):
    """
    Returns the number of occurrences of substr in str.

    Args:
        str (str): The input string.
        substr (str): The substring to count.

    Returns:
        int: The number of occurrences of substr in str.
    """
    return str.count(substr)


def substring_index(str, substr):
    """
    Returns the index of the first occurrence of substr in str.

    Args:
        str (str): The input string.
        substr (str): The substring to find.

    Returns:
        int: The index of the first occurrence of substr in str.
    """
    return str.find(substr)

def substring_index_last(str, substr):
    """
    Returns the index of the last occurrence of substr in str.

    Args:
        str (str): The input string.
        substr (str): The substring to find.

    Returns:
        int: The index of the last occurrence of substr in str.
    """
    return str.rfind(substr)


def substring_index_all(str, substr):
    """
    Returns a list of indices where substr occurs in str.

    Args:
        str (str): The input string.
        substr (str): The substring to find.

    Returns:
        list: A list of indices where substr occurs in str.
    """
    indices = []
    start = 0
    while True:
        index = str.find(substr, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices


def string_strip(str):
    """
    Removes leading and trailing whitespace from the input string.

    Args:
        str (str): The input string.

    Returns:
        str: The input string with leading and trailing whitespace removed.
    """
    return str.strip()


def string_lstrip(str):
    """
    Removes leading whitespace from the input string.

    Args:
        str (str): The input string.

    Returns:
        str: The input string with leading whitespace removed.
    """
    return str.lstrip()


def string_rstrip(str):
    """
    Removes trailing whitespace from the input string.

    Args:
        str (str): The input string.

    Returns:
        str: The input string with trailing whitespace removed.
    """
    return str.rstrip()
