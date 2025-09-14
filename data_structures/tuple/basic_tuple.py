"""
This module demonstrates basic operations on a tuple data structure in Python.
It includes creating a tuple, accessing elements, slicing, and unpacking.
- create_empty_tuple: Create an empty tuple.
- create_typle(elements): Create a tuple with given elements.
- access_tuple_elements(my_tuple, index): Access an element by index.
- slice_tuple(my_tuple, start, end): Slice the tuple from start to end.
- unpack_tuple(my_tuple): Unpack the tuple into individual variables.
- tuple_count(my_tuple, value): Count occurrences of a value in the tuple.
- tuple_index(my_tuple, value): Find the index of a value in the tuple.
"""

def create_empty_tuple():
    """Create and return a new empty tuple."""
    my_tuple = ()
    return my_tuple, f"Empty tuple created: {type(my_tuple)}"


def create_tuple(elements):
    """Create and return a tuple with the given elements."""
    my_tuple = tuple(elements)
    return my_tuple, f"Tuple created with elements: {my_tuple}"


def access_tuple_elements(my_tuple, index):
    """Access and return an element from the tuple by index."""
    try:
        element = my_tuple[index]
        return element, f"Element at index {index}: {element}"
    except IndexError:
        return None, f"Index {index} is out of range for the tuple."
    

def slice_tuple(my_tuple, start, end):
    """Return a slice of the tuple from start to end."""
    sliced_tuple = my_tuple[start:end]
    return sliced_tuple, f"Sliced tuple from index {start} to {end}: {sliced_tuple}"


def unpack_tuple(my_tuple):
    """Unpack the tuple into individual variables."""
    try:
        a, b, c = my_tuple
        return (a, b, c), f"Tuple unpacked into variables: a={a}, b={b}, c={c}"
    except ValueError:
        return None, "Tuple cannot be unpacked into three variables."
    

def tuple_count(my_tuple, value):
    """Count occurrences of a value in the tuple."""
    count = my_tuple.count(value)
    return count, f"Value {value} occurs {count} times in the tuple."


def tuple_index(my_tuple, value):
    """Find the index of the first occurrence of a value in the tuple."""
    try:
        index = my_tuple.index(value)
        return index, f"Value {value} found at index {index} in the tuple."
    except ValueError:
        return None, f"Value {value} not found in the tuple."
    
    
# Example usage
if __name__ == "__main__":
    empty_tuple, msg = create_empty_tuple()
    print(msg)

    my_tuple, msg = create_tuple([1, 2, 3, 4, 5])
    print(msg)

    element, msg = access_tuple_elements(my_tuple, 2)
    print(msg)

    sliced_tuple, msg = slice_tuple(my_tuple, 1, 4)
    print(msg)

    unpacked_vars, msg = unpack_tuple((10, 20, 30))
    print(msg)

    count, msg = tuple_count(my_tuple, 3)
    print(msg)

    index, msg = tuple_index(my_tuple, 4)
    print(msg)
