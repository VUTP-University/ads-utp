"""
This module provides basic functions to manipulate lists in Python.
- list_length: Returns the length of the list.
- list_append: Appends an item to the end of the list.
- list_pop: Removes and returns the last item from the list.
- list_insert: Inserts an item at a specified index in the list.
- list_remove: Removes the first occurrence of an item from the list.
- list_search: Searches for an item and returns its index or -1 if not found.
- list_sort: Returns a sorted copy of the list.
"""


def list_length(lst):
    """
    Returns the length of the input list.

    Args:
        lst (list): The input list.

    Returns:
        int: The length of the input list.
    """
    return len(lst)


def list_append(lst, item):
    """
    Appends an item to the end of the input list.

    Args:
        lst (list): The input list.
        item: The item to append.

    Returns:
        list: The input list with the item appended.
    """
    lst.append(item)
    return lst


def list_pop(lst):
    """
    Removes and returns the last item from the input list.

    Args:
        lst (list): The input list.

    Returns:
        item: The last item from the input list.
    """
    return lst.pop()


def list_insert(lst, index, item):
    """
    Inserts an item at the specified index in the input list.

    Args:
        lst (list): The input list.
        index (int): The index at which to insert the item.
        item: The item to insert.

    Returns:
        list: The input list with the item inserted.
    """
    lst.insert(index, item)
    return lst


def list_remove(lst, item):
    """
    Removes the first occurrence of an item from the input list.

    Args:
        lst (list): The input list.
        item: The item to remove.

    Returns:
        list: The input list with the item removed.
    """
    lst.remove(item)
    return lst


def list_search(lst, target):
    """
    Returns the index of the first occurrence of target in lst, or -1 if target is not in lst.

    Args:
        lst (list): The input list.
        target: The target element to search for.

    Returns:
        int: The index of the first occurrence of target in lst, or -1 if target is not in lst.
    """
    for i, elem in enumerate(lst):
        if elem == target:
            return i
    return -1


def list_sort(lst):
    """
    Returns a sorted copy of the input list.

    Args:
        lst (list): The input list.

    Returns:
        list: The sorted copy of the input list.
    """
    return sorted(lst)


# Example usage
if __name__ == "__main__":
    sample_list = [5, 3, 8, 1, 2]
    print("Original List:", sample_list) # Original List: [5, 3, 8, 1, 2]
    print("Length:", list_length(sample_list)) # Length: 5
    print("Append 4:", list_append(sample_list, 4)) # Append 4: [5, 3, 8, 1, 2, 4]
    print("Pop:", list_pop(sample_list)) # Pop: 4
    print("Insert 7 at index 2:", list_insert(sample_list, 2, 7)) # Insert 7 at index 2: [5, 3, 7, 8, 1, 2]
    print("Remove 3:", list_remove(sample_list, 3)) # Remove 3: [5, 7, 8, 1, 2]
    print("Search for 8:", list_search(sample_list, 8)) # Search for 8: 2
    print("Sorted List:", list_sort(sample_list)) # Sorted List: [1, 2, 5, 7, 8]