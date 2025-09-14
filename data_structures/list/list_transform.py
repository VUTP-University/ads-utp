"""
This module provides functions to manipulate and transform lists in Python.

- list_extend: Extends one list with another and returns the new list.
- replace_index: Replaces an element at a specified index with a new item and returns the new list.
- list_square: Returns a new list with each element squared. All elements must be numbers(integers or floats).

"""

def list_extend(lst1, lst2):
    """
    Returns a new list that is the result of extending lst1 with lst2.

    Args:
        lst1 (list): The first input list.
        lst2 (list): The second input list.

    Returns:
        list: The new list that is the result of extending lst1 with lst2.
    """
    return lst1 + lst2


def replace_index(lst, index, item):
    """
    Returns a new list where the element at the specified index is replaced with the given item.

    Args:
        lst (list): The input list.
        index (int): The index of the element to replace.
        item: The item to replace the element with.

    Returns:
        list: The new list with the element at the specified index replaced.
    """
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range")
    new_lst = lst.copy()
    new_lst[index] = item
    return new_lst


def list_square(lst):
    """
    Returns a new list where each element is the square of the corresponding element in the input list.

    Args:
        lst (list): The input list of numbers.

    Returns:
        list: The new list with each element squared.
    """
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numbers")
    
    return [x ** 2 for x in lst]


# Example usage
print("Extended list of [1, 2, 3] and [4, 5]:", list_extend([1, 2, 3], [4, 5]))  # Output: [1, 2, 3, 4, 5]
print("List after replacing index 2 with 10 in [1, 2, 3, 4]:", replace_index([1, 2, 3, 4], 2, 10))  # Output: [1, 2, 10, 4]
print("Squared list of [1, 2, 3, 4]:", list_square([1, 2, 3, 4]))  # Output: [1, 4, 9, 16]
print("Squared list of [1, 'a', 3]:", list_square([1, 'a', 3]))  # Raises ValueError