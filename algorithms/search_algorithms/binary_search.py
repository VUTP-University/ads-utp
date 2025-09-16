"""
This module implements the binary search algorithm.
It provides a function to search for a target value within a sorted list of numbers.
"""

def binary_search(arr, target):
    """
    Searches for a target value within a sorted list of numbers using the binary search algorithm.

    Parameters:
    arr (list): A sorted list of numbers to search within.
    target (int or float): The value to search for.

    Returns:
    int: The index of the target value if found; otherwise, -1.
    """
    left, right = 0, len(arr) - 1
    
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
    result_index = binary_search(sample_array, target_value)
    
    if result_index != -1:
        print(f"Element {target_value} found at index {result_index}.")
    else:
        print(f"Element {target_value} not found in the array.")