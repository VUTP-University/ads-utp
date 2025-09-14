# Algorithms and Data Structures with Python

A comprehensive educational library implementing various algorithms and data structures in Python. This project serves as a learning resource for computer science students and developers who want to understand fundamental data structures and algorithms through practical implementations.

## 🚀 Features

### Data Structures Implemented

- **Stack**: LIFO (Last In, First Out) data structure with push, pop, peek operations
- **Queue**: FIFO (First In, First Out) data structure with enqueue, dequeue operations  
- **Linked List**: Singly linked list with insertion, deletion, and traversal methods
- **Binary Search Tree (BST)**: Self-balancing tree structure with search, insert, delete operations
- **Dictionary**: Key-value pair data structure with hash table implementation
- **List**: Dynamic array implementation with indexing and transformation operations
- **String**: String manipulation utilities and indexing operations
- **Tuple**: Immutable sequence data structure operations
- **Set**: Collection of unique elements with set operations

### Key Features
- 📚 **Educational Focus**: Clean, well-documented implementations perfect for learning
- 🔍 **Comprehensive Examples**: Each data structure includes usage examples
- 🧪 **Modular Design**: Each data structure is implemented in separate modules
- 📖 **Detailed Documentation**: Extensive docstrings and comments throughout
- 🐍 **Pure Python**: No external dependencies required

## 📋 Requirements

- Python 3.8 or higher
- No external dependencies required

## 🛠️ Installation

### Clone the Repository
```bash
git clone https://github.com/VUTP-University/ads-utp.git
cd ads-utp
```

## 📚 Usage

### Basic Import and Usage

```python
# Import the test module to access all data structures
import test

# Or import specific data structures
from data_structures.stack.basic_stack import Stack
from data_structures.queue.basic_queue import Queue
from data_structures.linked_list.basic_linked_list import LinkedList
from binary_tree.binary_search_tree import BST
```

### Stack Example

```python
from data_structures.stack.basic_stack import Stack

# Create a new stack
stack = Stack()

# Add elements
stack.push(1)
stack.push(2)
stack.push(3)

# Access elements
print(stack.peek())    # Output: 3 (top element)
print(stack.pop())     # Output: 3 (removes and returns top)
print(stack.size())    # Output: 2
print(stack)           # Output: Stack([1, 2])
```

### Queue Example

```python
from data_structures.queue.basic_queue import Queue

# Create a new queue
queue = Queue()

# Add elements
queue.enqueue("first")
queue.enqueue("second")
queue.enqueue("third")

# Process elements
print(queue.front())       # Output: "first"
print(queue.dequeue())     # Output: "first" (removes and returns)
print(queue.size())        # Output: 2
```

### Binary Search Tree Example

```python
from binary_tree.binary_search_tree import BST

# Create a new BST
bst = BST()

# Insert values
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

# Traverse the tree
print("In-order:", bst.in_order_traversal())      # [3, 5, 7, 10, 15]
print("Pre-order:", bst.pre_order_traversal())    # [10, 5, 3, 7, 15]
print("Post-order:", bst.post_order_traversal())  # [3, 7, 5, 15, 10]

# Search for values
print(bst.search(7))    # True
print(bst.search(20))   # False

# Delete a value
bst.delete(5)
print("After deletion:", bst.in_order_traversal())  # [3, 7, 10, 15]
```

### Linked List Example

```python
from data_structures.linked_list.basic_linked_list import LinkedList

# Create a new linked list
ll = LinkedList()

# Add elements
ll.insert_at_beginning(1)
ll.insert_at_end(2)
ll.insert_at_end(3)

# Display and manipulate
ll.display()                    # Shows the list
print(ll.get_length())          # Output: 3
print(ll.search(2))             # Search for value 2
ll.delete_node(2)               # Delete node with value 2
```

## 📁 Project Structure

```
ads-utp/
├── data_structures/           # Core data structure implementations
│   ├── stack/                # Stack implementation
│   ├── queue/                # Queue implementation
│   ├── linked_list/          # Linked list implementations
│   ├── list/                 # Dynamic list operations
│   ├── dictionary/           # Dictionary/hash table
│   ├── string/               # String operations
│   ├── tuple/                # Tuple operations
│   └── set/                  # Set operations
├── binary_tree/              # Tree data structures
│   └── binary_search_tree.py # BST implementation
├── test.py                   # Main testing/import module
├── pyproject.toml           # Project configuration
├── LICENSE                  # License information
└── README.md               # This file
```

## 🧪 Running Tests

To test the functionality of the implemented data structures:

```bash
python test.py
```

You can also run individual module tests:

```bash
python data_structures/stack/basic_stack.py
python data_structures/queue/basic_queue.py
python binary_tree/binary_search_tree.py
```

## 📖 Learning Objectives

This library is designed to help you understand:

- **Time and Space Complexity**: Each implementation demonstrates different complexity characteristics
- **Algorithm Design Patterns**: Common patterns like recursion, iteration, and divide-and-conquer
- **Data Structure Applications**: Real-world use cases for each data structure
- **Python Programming**: Best practices for object-oriented programming in Python

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-algorithm`
3. **Add your implementation** with proper documentation and examples
4. **Write tests** for your new features
5. **Submit a pull request**

### Contribution Guidelines

- Follow the existing code style and documentation patterns
- Include comprehensive docstrings for all classes and methods
- Add usage examples in the `if __name__ == "__main__":` block
- Ensure your code works with Python 3.8+

## 📄 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## 👨‍💻 Author

**Aleksandar Karastoyanov**

## 🎯 Educational Use

This library is perfect for:

- **Computer Science Students**: Learning fundamental data structures and algorithms
- **Coding Interview Preparation**: Understanding common data structures asked in technical interviews
- **Teaching**: Educators can use these clean implementations as teaching materials
- **Self-Study**: Developers wanting to strengthen their understanding of data structures

## 🔗 Related Topics

- Algorithm Analysis and Big O Notation
- Object-Oriented Programming in Python
- Recursive vs. Iterative Solutions
- Memory Management and Efficiency

---

**Happy Learning! 🚀**

For questions, suggestions, or issues, please open an issue in the GitHub repository.
