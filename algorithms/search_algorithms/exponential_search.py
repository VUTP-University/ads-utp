"""
This module implements the exponential search algorithm.
It provides a function to search for a target value in a sorted list of numbers.
"""


def exponential_search(arr, target):
    """
    Searches for a target value in a sorted list of numbers using the exponential search algorithm.

    Parameters:
    arr (list): A sorted list of numbers.
    target (int or float): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    if len(arr) == 0:
        return -1

    # If the target is at the first location
    if arr[0] == target:
        return 0

    # Find range for binary search by repeated doubling
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2

    # Call binary search for the found range
    return binary_search(arr, target, index // 2, min(index, len(arr) - 1))


def binary_search(arr, target, left, right):
    """
    A helper function to perform binary search on a subarray.

    Parameters:
    arr (list): A sorted list of numbers.
    target (int or float): The value to search for.
    left (int): The starting index of the subarray.
    right (int): The ending index of the subarray.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    while left <= right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1


# Example usage
if __name__ == "__main__":
    sample_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target_value = 7
    result_index = exponential_search(sample_array, target_value)
    if result_index != -1:
        print(f"Element {target_value} found at index {result_index}.")
    else:
        print(f"Element {target_value} not found in the array.")