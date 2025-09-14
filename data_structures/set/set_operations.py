"""
This module demonstrates various set operations in Python.
It includes union, intersection, difference, and symmetric difference operations.
- set_union(set1, set2): Return the union of two sets.
- set_intersection(set1, set2): Return the intersection of two sets.
- set_difference(set1, set2): Return the difference of two sets (elements in set1 but not in set2).
- set_symmetric_difference(set1, set2): Return the symmetric difference of two sets (elements in either set1 or set2 but not in both).
"""

def set_union(set1, set2):
    """Return the union of two sets."""
    return set1 | set2


def set_intersection(set1, set2):
    """Return the intersection of two sets."""
    return set1 & set2


def set_difference(set1, set2):
    """Return the difference of two sets (elements in set1 but not in set2)."""
    return set1 - set2


def set_symmetric_difference(set1, set2):
    """Return the symmetric difference of two sets (elements in either set1 or set2 but not in both)."""
    return set1 ^ set2


# Example usage
if __name__ == "__main__":
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Union:", set_union(set_a, set_b))
    print("Intersection:", set_intersection(set_a, set_b))
    print("Difference (A - B):", set_difference(set_a, set_b))
    print("Symmetric Difference:", set_symmetric_difference(set_a, set_b))