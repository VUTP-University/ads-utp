"""
This module defines a Graph class for representing and manipulating directed graphs.
It includes methods for adding nodes and edges.
It also includes a method to display the graph's adjacency list.
"""

class Graph():
    """
    A class to represent a directed graph using an adjacency list.
    
    Attributes:
    graph (dict): A dictionary where keys are nodes and values are lists of tuples representing edges and their weights.
    
    Methods:
    add_node(node): Adds a node to the graph.
    add_edge(from_node, to_node, weight): Adds a directed edge from from_node to to_node with a specified weight.
    display(): Displays the adjacency list of the graph.
    
    """
    
    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.graph = {}
        self.directed = True
        
        
    def add_node(self, node):
        """
        Adds a node to the graph.
        
        Parameters:
        node: The node to be added to the graph.
        """
        if node not in self.graph:
            self.graph[node] = []
        
            
    def add_edge(self, from_node, to_node, weigth=None):
        """
        Adds a directed edge from from_node to to_node with a specified weight(None by default).
        
        Parameters:
        from_node: The starting node of the edge.
        to_node: The ending node of the edge.
        weight: The weight of the edge(None if not passed).
        """
        if from_node not in self.graph:
            self.add_node(from_node)
        if to_node not in self.graph:
            self.add_node(to_node)
        self.graph[from_node].append((to_node, weigth))
        
    
    def get_neighbors(self, node):
        """
        Returns the neighbors of a given node.
        
        Parameters:
        node: The node whose neighbors are to be returned.
        
        Returns:
        list: A list of tuples representing the neighbors and their edge weights.
        """
        return self.graph.get(node, [])
    
    
    def has_path(self, start_node, end_node, visited=None):
        """
        Determines if there is a path from start_node to end_node using Depth-First Search (DFS).
        
        Parameters:
        start_node: The starting node of the path.
        end_node: The ending node of the path.
        visited: A set of visited nodes to avoid cycles (used in recursion).
        
        Returns:
        bool: True if a path exists, False otherwise.
        """
        if visited is None:
            visited = set()
        
        if start_node == end_node:
            return True
        
        visited.add(start_node)
        
        for neighbor, _ in self.get_neighbors(start_node):
            if neighbor not in visited:
                if self.has_path(neighbor, end_node, visited):
                    return True
        
        return False
    
        
    def display(self):
        """
        Displays the adjacency list of the graph.
        """
        for node, edges in self.graph.items():
            print(f"{node} -> {', '.join(map(str, edges))}")
            
    
# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 5)
    graph.add_edge("B", "D", 3)
    graph.add_edge("B", "E", 4)
    graph.add_edge("C", "D", 7)
    graph.add_edge("C", "F", 8)
    graph.add_edge("D", "E", 6)
    graph.add_edge("E", "F", 2)
    graph.display()
            
    