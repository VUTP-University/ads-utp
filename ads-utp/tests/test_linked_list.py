import pytest
from data_structures.linked_list import LinkedList

def test_linked_list_operations():
    # Create a linked list
    ll = LinkedList()
    
    # Test adding elements
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert ll.to_list() == [10, 20, 30]
    
    # Test removing an element
    ll.remove(20)
    assert ll.to_list() == [10, 30]

    # Test searching for an element
    assert ll.find(10) is not None
    assert ll.find(20) is None

def test_edge_cases():
    ll = LinkedList()
    
    # Test removing from an empty list
    ll.remove(100)  # Should handle gracefully
    
    # Test searching in an empty list
    assert ll.find(100) is None

if __name__ == "__main__":
    pytest.main()