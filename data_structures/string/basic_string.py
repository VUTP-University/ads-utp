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



# Example usage
print("String Length:", string_length("Hello, World!"))  # Output: 13
print("Substring Count:", substring_count("Hello, World! Hello!", "Hello"))  # Output: 2
print("Substring Index:", substring_index("Hello, World!", "World"))  # Output: 7
print("Substring Index Last:", substring_index_last("Hello, World! Hello!", "Hello"))  # Output: 13
print("Substring Index All:", substring_index_all("Hello, World! Hello!", "Hello"))  # Output: [0, 13]
print("Substring Index All (not found):", substring_index_all("Hello, World!", "Python"))  # Output: []
print("Substring Index All (overlapping):", substring_index_all("aaaaa", "aa"))  # Output: [0, 1, 2, 3]
print("Substring Index All (empty substring):", substring_index_all("Hello", ""))  # Output: [0, 1, 2, 3, 4, 5]
print("Substring Index All (empty string):", substring_index_all("", "a"))  # Output: []
print("Substring Index All (both empty):", substring_index_all("", ""))  # Output: [0]
print("Substring Index All (no occurrence):", substring_index_all("abcdef", "gh"))  # Output: []
print("Substring Index All (single character):", substring_index_all("banana", "a"))  # Output: [1, 3, 5]
print("Substring Index All (case sensitive):", substring_index_all("Hello hello HeLLo", "Hello"))  # Output: [0]
print("Substring Index All (special characters):", substring_index_all("!@#$%^&*()!@#", "!@"))  # Output: [0, 10]
print("Substring Index All (long substring):", substring_index_all("ababababab", "abab"))  # Output: [0, 2, 4]
print("String Strip:", string_strip("   Hello, World!   "))  # Output: "Hello, World!"
print("String LStrip:", string_lstrip("   Hello, World!   "))  # Output: "Hello, World!   "
print("String RStrip:", string_rstrip("   Hello, World!   "))  # Output: "   Hello, World!"
print("String Strip (no whitespace):", string_strip("Hello"))  # Output: "Hello"