"""
This module implements the bubble sort algorithm.
It provides a function to sort a list of numbers in ascending order using the bubble sort technique.
"""

import random

def bubble_sort(arr):
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.

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
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    
    return sorted_arr

# Example usage
if __name__ == "__main__":
    sample_array = [random.randint(1, 10_000) for _ in range(100)]
    print("Original array:", sample_array)
    sorted_array = bubble_sort(sample_array)
    print("\nSorted array:", sorted_array)