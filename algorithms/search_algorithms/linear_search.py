"""
This module implements the linear search algorithm.
It provides a function to search for a target value in a list of numbers using the linear search technique.
"""

def linear_search(arr, target):
    """
    Searches for a target value in a list of numbers using the linear search algorithm.

    Parameters:
    arr (list): A list of numbers to search through.
    target (int/float): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def sentinel_linear_search(arr, target):
    """
    Searches for a target value in a list of numbers using the sentinel linear search algorithm.

    Parameters:
    arr (list): A list of numbers to search through.
    target (int/float): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    n = len(arr)
    if n == 0:
        return -1

    # Work on a copy to avoid modifying the original array
    arr_copy = arr[:]
    last = arr_copy[-1]
    arr_copy[-1] = target

    index = 0
    while arr_copy[index] != target:
        index += 1

    # Restore the last element (not strictly necessary for the copy, but for completeness)
    arr_copy[-1] = last

    if index < n - 1 or arr[-1] == target:
        return index
    return -1


# Example usage
if __name__ == "__main__":
    sample_array = [10, 23, 45, 70, 11, 15]
    target_value = 70
    result_index = linear_search(sample_array, target_value)
    linear_search_index = sentinel_linear_search(sample_array, target_value)
    
    if result_index != -1:
        print(f"Element {target_value} found at index {result_index}.")
    else:
        print(f"Element {target_value} not found in the array.")
    
    if linear_search_index != -1:
        print(f"Element {target_value} found at index {linear_search_index} using sentinel search.")
    else:
        print(f"Element {target_value} not found in the array using sentinel search.")

