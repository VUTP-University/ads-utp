"""
This module implements the heap sort algorithm.
It provides a function to sort a list of numbers in ascending order using the heap sort technique.
"""

import random


def heapify(arr, n, i):
    """
    Helper function to maintain the heap property of a subtree rooted at index i.
    
    Parameters:
    arr (list): The list representing the heap.
    n (int): The size of the heap.
    i (int): The index of the root of the subtree.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Sorts a list of numbers in ascending order using the heap sort algorithm.

    Parameters:
    arr (list): A list of numbers to be sorted.

    Returns:
    list: A new list containing the sorted numbers.
    """
    n = len(arr)
    # Create a copy of the array to avoid modifying the original
    sorted_arr = arr.copy()

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(sorted_arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        # Move current root to end
        sorted_arr[i], sorted_arr[0] = sorted_arr[0], sorted_arr[i]  # Swap
        # Call heapify on the reduced heap
        heapify(sorted_arr, i, 0)

    return sorted_arr


# Example usage
if __name__ == "__main__":
    sample_array = [random.randint(1, 10_000) for _ in range(100)]
    print("Original array:", sample_array)
    sorted_array = heap_sort(sample_array)
    print("\nSorted array:", sorted_array)
