import pytest
from data_structures.linked_list import LinkedList, Node


def test_append_single_element():
    """
    Test that a single element can be appended to an empty linked list.

    Ensures:
    - head is no longer None
    - head contains the correct data
    - next pointer of head is None
    """
    ll = LinkedList()
    ll.append(10)
    assert ll.head is not None
    assert ll.head.data == 10
    assert ll.head.next is None


def test_append_multiple_elements():
    """
    Test appending multiple elements to the linked list.

    Ensures:
    - Elements are stored in insertion order
    - All nodes are linked correctly
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]


def test_remove_head():
    """
    Test removing the head element of the linked list.

    Ensures:
    - Head is updated to point to the next node
    - Removed node is no longer in the list
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.remove(1)
    assert ll.to_list() == [2]
    assert ll.head.data == 2


def test_remove_middle_element():
    """
    Test removing a middle element from the linked list.

    Ensures:
    - Only the first occurrence of the key is removed
    - List links remain intact
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.remove(2)
    assert ll.to_list() == [1, 3]


def test_remove_non_existent_element():
    """
    Test attempting to remove an element not present in the list.

    Ensures:
    - List remains unchanged
    - No exceptions are raised
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.remove(3)
    assert ll.to_list() == [1, 2]


def test_find_existing_node():
    """
    Test finding a node that exists in the list.

    Ensures:
    - The correct node is returned
    - The data matches the search key
    """
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    found = ll.find(10)
    assert found is not None
    assert found.data == 10


def test_find_nonexistent_node():
    """
    Test searching for a node that does not exist.

    Ensures:
    - Function returns None
    - No exception is raised
    """
    ll = LinkedList()
    ll.append(5)
    assert ll.find(99) is None


def test_to_list_empty():
    """
    Test converting an empty linked list to a Python list.

    Ensures:
    - The result is an empty list
    """
    ll = LinkedList()
    assert ll.to_list() == []


def test_to_list_non_empty():
    """
    Test converting a non-empty linked list to a Python list.

    Ensures:
    - All elements are returned in the correct order
    - Result is of type list
    """
    ll = LinkedList()
    ll.append('a')
    ll.append('b')
    assert ll.to_list() == ['a', 'b']


if __name__ == "__main__":
    pytest.main()
