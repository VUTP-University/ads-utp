"""
This module implements a basic stack data structure with common operations.
"""

class Stack():
    """A simple stack implementation using a list.
    
    Attributes:
        items (list): A list to store stack elements.
        
    Methods:
        is_empty(): Check if the stack is empty.
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item from the stack.
        peek(): Return the top item without removing it.
        size(): Return the number of items in the stack.
        clear(): Remove all items from the stack.
        get_items(): Return a list of all items in the stack.
        __str__(): Return a string representation of the stack.
    """
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self.items = []
    
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def push(self, item) -> None:
        """Add an item to the top of the stack."""
        self.items.append(item)
        
    def pop(self):
        """Remove and return the top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)
    
    def clear(self) -> None:
        """Remove all items from the stack."""
        self.items.clear()
        
    def get_items(self) -> list:
        """Return a list of all items in the stack."""
        return self.items.copy()
    
    def __str__(self) -> str:
        """Return a string representation of the stack."""
        return "Stack(" + str(self.items) + ")"
    

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)         # Output: Stack([1, 2, 3])
    print(stack.pop())   # Output: 3
    print(stack.peek())  # Output: 2
    print(stack.size())  # Output: 2
    print(stack.is_empty())  # Output: False
    stack.clear()
    print(stack.is_empty())  # Output: True