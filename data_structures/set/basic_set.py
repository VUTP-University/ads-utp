"""
This module demonstrates basic operations on a set data structure in Python.
It includes creating a set, adding elements, removing elements, and checking for membership.
- create_empty_set: Create an empty set.
- create_new_set(elements): Create a new set with given elements.
- add_element(s, element): Add an element to the set.
- discard_element(s, element): Remove an element from the set if it exists.
- update_set(s, elements): Update the set with multiple elements.
- is_member(s, element): Check if an element is a member of the set.
"""

def create_empty_set():
    """Create and return a new empty set."""
    return set()


def create_new_set(elements):
    """Create and return a new set with the given elements."""
    return set(elements)


def add_element(s, element):
    """Add an element to the set."""
    s.add(element)
    
    
def discard_element(s, element):
    """Remove an element from the set if it exists. Does nothing if the element is not found."""
    s.discard(element)
    

def update_set(s, elements):
    """Update the set with multiple elements."""
    s.update(elements)
    

def is_member(s, element):
    """Check if an element is a member of the set."""
    return element in s
    
# Example usage
print("Creating an empty set:", create_empty_set())
print("Creating a new set with elements [1, 2, 3]:", create_new_set([1, 2, 3]))
print("Adding element 4 to the set {1, 2, 3}:", add_element(create_new_set([1, 2, 3]), 4))
print("Discarding element 2 from the set {1, 2, 3}:", discard_element(create_new_set([1, 2, 3]), 2))
print("Updating the set {1, 2, 3} with elements [4, 5]:", update_set(create_new_set([1, 2, 3]), [4, 5]))
print("Checking if 3 is a member of the set {1, 2, 3}:", is_member(create_new_set([1, 2, 3]), 3))