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
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Set Union:", set_union(set_a, set_b))
print("Set Intersection:", set_intersection(set_a, set_b))
print("Set Difference (A - B):", set_difference(set_a, set_b))
print("Set Symmetric Difference:", set_symmetric_difference(set_a, set_b))