def list_index(lst, item):
    """
    Returns the index of the first occurrence of an item in the input list.

    Args:
        lst (list): The input list.
        item: The item to search for.

    Returns:
        int: The index of the first occurrence of the item, or -1 if not found.
    """
    for i, x in enumerate(lst):
        if x == item:
            return i
    return -1


def list_slice(lst, start, end):
    """
    Returns a slice of the input list from start to end.

    Args:
        lst (list): The input list.
        start (int): The start index of the slice.
        end (int): The end index of the slice.

    Returns:
        list: The slice of the input list.
    """
    return lst[start:end]


def list_reverse(lst):
    """
    Returns a reversed copy of the input list.

    Args:
        lst (list): The input list.

    Returns:
        list: The reversed copy of the input list.
    """
    return lst[::-1]


# Example usage
print("Index of 3 in [1, 2, 3, 4, 3]:", list_index([1, 2, 3, 4, 3], 3))  # Output: 2
print("Slice of [1, 2, 3, 4, 5] from index 1 to 4:", list_slice([1, 2, 3, 4, 5], 1, 4))  # Output: [2, 3, 4]
print("Reversed list of [1, 2, 3, 4, 5]:", list_reverse([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]