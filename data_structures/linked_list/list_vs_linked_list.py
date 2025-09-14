"""
This module compares the usage of Python's built-in list with a custom singly linked list implementation.
It demonstrates creation, insertion, access, modification, and deletion of elements in both data structures
and compares their performance and runtime for various operations.
"""

import time
import random
from basic_linked_list import LinkedList

ll = LinkedList()
py_list = []

def measure_time(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


@measure_time
def test_linked_list_operations():
    """Test basic operations on the linked list."""
    # Insertion
    for i in range(1000):
        ll.insert_at_end(i)
    for i in range(1000, 2000):
        ll.insert_at_beginning(i)

    # Access
    for i in range(500):
        current = ll.head
        for _ in range(i):
            if current:
                current = current.next

    # Modification
    current = ll.head
    while current:
        if current.data % 2 == 0:
            current.data *= 2
        current = current.next

    # Deletion
    for i in range(500):
        ll.delete_node(i)
        


@measure_time
def test_list_operations():
    """Test basic operations on the Python list."""
    # Insertion
    for i in range(1000):
        py_list.append(i)
    for i in range(1000, 2000):
        py_list.insert(0, i)

    # Access
    for i in range(500):
        _ = py_list[i]

    # Modification
    for i in range(len(py_list)):
        if py_list[i] % 2 == 0:
            py_list[i] *= 2

    # Deletion
    for i in range(500):
        if i in py_list:
            py_list.remove(i)
            
if __name__ == "__main__":
    print("Testing Linked List Operations:")
    test_linked_list_operations()
    
    print("\nTesting Python List Operations:")
    test_list_operations()
    
    
"""
But built-in lists are generally more efficient for most use cases due to their optimized implementation in C and better cache locality.

In this comparison, we see that while linked lists provide flexibility in dynamic memory allocation and ease of insertion/deletion, 
they come with overhead in terms of memory usage and access time.

Bult-in lists are implemented as dynamic arrays, which allow for efficient indexing and better performance for a wide range of operations.
"""