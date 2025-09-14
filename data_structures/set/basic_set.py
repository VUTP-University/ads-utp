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
    my_set = set()
    return my_set, f"Empty set created: {type(my_set)}"


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
if __name__ == "__main__":
    empty_set, msg = create_empty_set()
    print(msg)
    
    my_set = create_new_set([1, 2, 3])
    print(f"New set created: {my_set}")
    
    add_element(my_set, 4)
    print(f"Set after adding 4: {my_set}")
    
    discard_element(my_set, 2)
    print(f"Set after discarding 2: {my_set}")
    
    update_set(my_set, [5, 6])
    print(f"Set after updating with [5, 6]: {my_set}")
    
    print(f"Is 3 a member of the set? {'Yes' if is_member(my_set, 3) else 'No'}")
    print(f"Is 2 a member of the set? {'Yes' if is_member(my_set, 2) else 'No'}")