"""
This module defines a Binary Search Tree (BST) with methods for insertion, search, 
in-order traversal, pre-order traversal, post-order traversal, and deletion of nodes.
"""


class BST():
    """A Binary Search Tree (BST) implementation.
    
    Attributes:
        root (Node): The root node of the BST.
    
    Methods:
        insert(value): Inserts a value into the BST.
        search(value): Searches for a value in the BST.
        in_order_traversal(): Returns a list of values in in-order traversal.
        pre_order_traversal(): Returns a list of values in pre-order traversal.
        post_order_traversal(): Returns a list of values in post-order traversal.
        delete(value): Deletes a value from the BST.
    """
    
    def __init__(self):
        """Initializes an empty BST."""
        self.root = None
        
    class Node:
        """A node in the BST.
        
        Attributes:
            value: The value of the node.
            left (Node): The left child node.
            right (Node): The right child node.
        """
        
        def __init__(self, value):
            """Initializes a node with a given value."""
            self.value = value
            self.left = None
            self.right = None
            
    def insert(self, value):
        """Inserts a value into the BST.
        
        Args:
            value: The value to be inserted.
        """
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_rec(self.root, value)
    
    def _insert_rec(self, node, value):
        """Private helper method for recursive insertion."""
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_rec(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_rec(node.right, value)
        # If value is equal, do not insert duplicates
    
    def search(self, value):
        """Searches for a value in the BST.
        
        Args:
            value: The value to be searched.
        
        Returns:
            bool: True if the value is found, False otherwise.
        """
        return self._search_rec(self.root, value)
    
    def _search_rec(self, node, value):
        """Private helper method for recursive search."""
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_rec(node.left, value)
        else:
            return self._search_rec(node.right, value)
    
    def _search_rec(self, node, value):
        """Private helper method for recursive search."""
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_rec(node.left, value)
        else:
            return self._search_rec(node.right, value)
    
    def in_order_traversal(self):
        """Returns a list of values in in-order traversal.
        
        Returns:
            list: A list of values in in-order traversal.
        """
        result = []
        self._in_order_rec(self.root, result)
        return result
    
    def _in_order_rec(self, node, result):
        """Private helper method for in-order traversal."""
        if node:
            self._in_order_rec(node.left, result)
            result.append(node.value)
            self._in_order_rec(node.right, result)
    
    def pre_order_traversal(self):
        """Returns a list of values in pre-order traversal.
        
        Returns:
            list: A list of values in pre-order traversal.
        """
        result = []
        self._pre_order_rec(self.root, result)
        return result
    
    def _pre_order_rec(self, node, result):
        """Private helper method for pre-order traversal."""
        if node:
            result.append(node.value)
            self._pre_order_rec(node.left, result)
            self._pre_order_rec(node.right, result)
    
    def post_order_traversal(self):
        """Returns a list of values in post-order traversal.
        
        Returns:
            list: A list of values in post-order traversal.
        """
        result = []
        self._post_order_rec(self.root, result)
        return result
    
    def _post_order_rec(self, node, result):
        """Private helper method for post-order traversal."""
        if node:
            self._post_order_rec(node.left, result)
            self._post_order_rec(node.right, result)
            result.append(node.value)
    
    def delete(self, value):
        """Deletes a value from the BST.
        
        Args:
            value: The value to be deleted.
        """
        self.root = self._delete_rec(self.root, value)

    def _delete_rec(self, node, value):
        """Private helper method for recursive deletion."""
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete_rec(node.left, value)
        elif value > node.value:
            node.right = self._delete_rec(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_rec(node.right, temp.value)
        
        return node
    
    def _min_value_node(self, node):
        """Helper method to find the node with the minimum value in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current


# Example usage:
if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    
    print("In-order Traversal:", bst.in_order_traversal())  # Output: [3, 5, 7, 10, 15]
    print("Pre-order Traversal:", bst.pre_order_traversal())  # Output: [10, 5, 3, 7, 15]
    print("Post-order Traversal:", bst.post_order_traversal())  # Output: [3, 7, 5, 15, 10]
    
    print("Search for 7:", bst.search(7))  # Output: True
    print("Search for 20:", bst.search(20))  # Output: False
    
    bst.delete(5)
    print("In-order Traversal after deleting 5:", bst.in_order_traversal())  # Output: [3, 7, 10, 15]
    print("Search for 5 after deletion:", bst.search(5))  # Output: False
    