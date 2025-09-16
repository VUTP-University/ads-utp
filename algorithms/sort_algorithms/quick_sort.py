"""
This module implements the quick sort algorithm.
It provides a function to sort a list of numbers in ascending order using the quick sort technique.
"""

import random


def quick_sort(arr):
    """
    Sorts a list of numbers in ascending order using the quick sort algorithm.

    Parameters:
    arr (list): A list of numbers to be sorted.

    Returns:
    list: A new list containing the sorted numbers.
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element from the array
        pivot = arr[len(arr) // 2]
        # Partition the array into three lists
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursively apply quick_sort to the left and right lists, then concatenate
        return quick_sort(left) + middle + quick_sort(right)


# Example usage
if __name__ == "__main__":
    sample_array = [random.randint(1, 10_000) for _ in range(100)]
    print("Original array:", sample_array)
    sorted_array = quick_sort(sample_array)
    print("\nSorted array:", sorted_array)