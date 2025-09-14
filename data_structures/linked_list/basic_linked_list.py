"""
This module demonstrates the basic usage of a singly linked list, including creation, insertion, 
access, modification, and deletion of nodes.
"""


class LinkedList():
    """A simple singly linked list implementation.
    Each node contains data and a reference to the next node.
    
    Attributes:
    - head: The head (first node) of the linked list.
    - next: Reference to the next node in the list.
    
    Methods:
    - insert_at_beginning(data): Insert a new node at the beginning of the list.
    - insert_at_end(data): Insert a new node at the end of the list.
    - delete_node(key): Delete the first node with the specified key (data).
    - search(key): Search for a node with the specified key (data).
    - display(): Display the linked list.
    - get_length(): Return the length of the linked list.
    
    """

    class Node:
        """A node in a singly linked list."""
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node with the given data at the beginning of the list."""
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        """Delete the first node with the specified key (data)."""
        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if not current:
            print(f"Node with data {key} not found.")
            return

        if previous:
            previous.next = current.next
        else:
            self.head = current.next

    def search(self, key):
        """Search for a node with the specified key (data)."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def get_length(self):
        """Return the length of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    
# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    
    # Inserting nodes
    ll.insert_at_end(10)
    ll.insert_at_beginning(20)
    ll.insert_at_end(30)
    
    # Displaying the linked list
    print("Linked List:")
    ll.display()
    
    # Searching for a node
    print("Searching for 20:", ll.search(20))
    print("Searching for 40:", ll.search(40))
    
    # Deleting a node
    ll.delete_node(20)
    print("Linked List after deleting 20:")
    ll.display()
    
    # Getting the length of the linked list
    print("Length of Linked List:", ll.get_length())