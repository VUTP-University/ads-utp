"""
This module implements the counting sort algorithm.
It provides a function to sort a list of non-negative integers in ascending order 
using the counting sort technique.
"""

import random

def counting_sort(arr):
    """
    Sorts a list of non-negative integers in ascending order using the counting sort algorithm.

    Parameters:
    arr (list): A list of non-negative integers to be sorted.

    Returns:
    list: A new list containing the sorted integers.
    """
    if not arr:
        return []

    # Find the maximum value in the array to determine the range of the count array
    max_val = max(arr)
    
    # Initialize the count array with zeros
    count = [0] * (max_val + 1)
    
    # Store the count of each number in the count array
    for num in arr:
        count[num] += 1
    
    # Build the sorted array
    sorted_arr = []
    for i, cnt in enumerate(count):
        sorted_arr.extend([i] * cnt)
    
    return sorted_arr

# Example usage
if __name__ == "__main__":
    sample_array = [random.randint(0, 1000) for _ in range(100)]
    print("Original array:", sample_array)
    sorted_array = counting_sort(sample_array)
    print("\nSorted array:", sorted_array)