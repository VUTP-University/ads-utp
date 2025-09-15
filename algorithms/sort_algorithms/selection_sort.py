"""
This module implements the selection sort algorithm.
It provides a function to sort a list of numbers in ascending order using the selection sort technique.
"""

import random


def selection_sort(arr):
    """
    Sorts a list of numbers in ascending order using the selection sort algorithm.

    Parameters:
    arr (list): A list of numbers to be sorted.

    Returns:
    list: A new list containing the sorted numbers.
    """
    n = len(arr)
    # Create a copy of the array to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    
    return sorted_arr


# Example usage
if __name__ == "__main__":
    sample_array = [random.randint(1, 10_000) for _ in range(100)]
    print("Original array:", sample_array)
    sorted_array = selection_sort(sample_array)
    print("\nSorted array:", sorted_array)