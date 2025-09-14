"""
This module implements a basic queue data structure with common operations.
"""

class Queue():
    """A simple queue implementation using a list.
    
    Attributes:
        items (list): A list to store queue elements.
        
    Methods:
        is_empty(): Check if the queue is empty.
        enqueue(item): Add an item to the end of the queue.
        dequeue(): Remove and return the front item from the queue.
        front(): Return the front item without removing it.
        size(): Return the number of items in the queue.
        clear(): Remove all items from the queue.
        get_items(): Return a list of all items in the queue.
        __str__(): Return a string representation of the queue.
    """
    
    def __init__(self) -> None:
        """Initialize an empty queue."""
        self.items = []
    
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    
    def enqueue(self, item) -> None:
        """Add an item to the end of the queue."""
        self.items.append(item)
        
        
    def dequeue(self):
        """Remove and return the front item from the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
    
    
    def front(self):
        """Return the front item without removing it.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self.items)
    
    
    def clear(self) -> None:
        """Remove all items from the queue."""
        self.items.clear()
        
        
    def get_items(self) -> list:
        """Return a list of all items in the queue."""
        return self.items.copy()
    
    
    def __str__(self) -> str:
        """Return a string representation of the queue."""
        return "Queue(" + str(self.items) + ")"
    
    
# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)            # Output: Queue([1, 2, 3])
    print(q.dequeue())  # Output: 1
    print(q.front())    # Output: 2
    print(q.size())     # Output: 2
    print(q.is_empty()) # Output: False
    q.clear()
    print(q.is_empty()) # Output: True
    
