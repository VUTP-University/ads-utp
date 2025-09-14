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
print("List Length:", list_length([1, 2, 3, 4]))  # Output: 4
print("List Append:", list_append([1, 2, 3], 4))  # Output: [1, 2, 3, 4]
print("List Pop:", list_pop([1, 2, 3, 4]))        # Output: 4
print("List Insert:", list_insert([1, 2, 4], 2, 3)) # Output: [1, 2, 3, 4]
print("List Remove:", list_remove([1, 2, 3, 4], 3)) # Output: [1, 2, 4]
print("List Search:", list_search([1, 2, 3, 4], 3)) # Output: 2
print("List Sort:", list_sort([4, 2, 3, 1]))       # Output: [1, 2, 3, 4]
