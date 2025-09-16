"""
This module implements the Fibonacci search algorithm.
It provides a function to search for a target value in a sorted list using the Fibonacci search technique.
"""


def fibonacci_search(arr, target):
    """
    Searches for a target value in a sorted list using the Fibonacci search algorithm.

    Parameters:
    arr (list): A sorted list of numbers where the search is performed.
    target (int or float): The value to search for in the list.

    Returns:
    int: The index of the target value if found; otherwise, -1.
    """
    n = len(arr)

    # Initialize Fibonacci numbers
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number

    # Find the smallest Fibonacci number greater than or equal to n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    # While there are elements to be inspected
    while fib_m > 1:
        # Calculate the index to be compared
        i = min(offset + fib_m2, n - 1)

        # If target is greater than the value at index i, cut the subarray after i
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        # If target is less than the value at index i, cut the subarray before i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1

        # Element found at index i
        else:
            return i

    # Comparing the last element with target
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    # Element not found
    return -1


# Example usage
if __name__ == "__main__":
    sample_array = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    target_value = 85
    result_index = fibonacci_search(sample_array, target_value)
    if result_index != -1:
        print(f"Target {target_value} found at index: {result_index}")
    else:
        print("Target not found in the array.")