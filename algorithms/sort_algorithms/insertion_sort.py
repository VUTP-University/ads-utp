"""
This module implements the insertion sort algorithm.
It provides a function to sort a list of numbers in ascending order using the insertion sort technique.
"""

import random


def insertion_sort(arr):
    """
    Sorts a list of numbers in ascending order using the insertion sort algorithm.

    Parameters:
    arr (list): A list of numbers to be sorted.

    Returns:
    list: A new list containing the sorted numbers.
    """
    # Create a copy of the array to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        # Move elements of sorted_arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < sorted_arr[j]:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    
    return sorted_arr


# Example usage
if __name__ == "__main__":
    sample_array = [random.randint(1, 10_000) for _ in range(100)]
    print("Original array:", sample_array)
    sorted_array = insertion_sort(sample_array)
    print("\nSorted array:", sorted_array)