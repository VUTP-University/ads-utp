class Node:
    """
    Represents a single node in the linked list.

    Attributes:
        data : Stores the value of the node.
        next : Points to the next node in the list (initially None).
    """
    def __init__(self, data):
        self.data = data  # Assign value to the node
        self.next = None  # Initialize next as None


class LinkedList:
    """
    A simple implementation of a singly linked list.

    Attributes:
        head : Points to the first node in the list (initially None).

    Methods:
        append(data): Adds a new node with the given data at the end of the list.
        remove(key): Removes the first occurrence of a node with the specified key.
        find(key): Searches for a node containing the specified key.
        to_list(): Converts the linked list into a Python list.
        display(): Prints the linked list in a readable format.
    """
    def __init__(self):
        self.head = None  # Initialize head as None

    def append(self, data):
        """Adds a new node containing the given data at the end of the linked list."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
    
    def remove(self, key):
        """Removes the first occurrence of a node with the specified key from the list."""
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        if temp is None:
            return
        
        prev.next = temp.next
        temp = None

    def find(self, key):
        """Searches for a node containing the specified key."""
        temp = self.head
        while temp:
            if temp.data == key:
                return temp  # Return the node if found
            temp = temp.next
        return None  # Return None if not found

    def to_list(self):
        """Converts the linked list into a Python list."""
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    def display(self):
        """Prints the elements of the linked list in a readable format."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

