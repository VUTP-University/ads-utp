"""
This module provides functions for indexing and slicing lists in Python.
It includes functions to find the index of an item, slice a list, and reverse a list.
- list_index(lst, item): Returns the index of the first occurrence of an item in the list.
- list_slice(lst, start, end): Returns a slice of the list from start to end.
- list_reverse(lst): Returns a reversed copy of the list.
"""

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
if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]

    # Find index of an item
    index = list_index(my_list, 30)
    print(f"Index of 30: {index}")  # Output: Index of 30: 2

    # Slice the list
    sliced = list_slice(my_list, 1, 4)
    print(f"Sliced list (1 to 4): {sliced}")  # Output: Sliced list (1 to 4): [20, 30, 40]

    # Reverse the list
    reversed_list = list_reverse(my_list)
    print(f"Reversed list: {reversed_list}")  # Output: Reversed list: [50, 40, 30, 20, 10]