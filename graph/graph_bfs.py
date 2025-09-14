"""
This module represents the Breadth-First Search (BFS) algorithm to traverse the graph.
"""

from graph import Graph

def graph_bfs(graph, start_node):
    """
    Performs Breadth-First Search (BFS) on the graph starting from the specified node.
    
    Parameters:
    graph: The graph to be traversed.
    start_node: The node from which to start the BFS traversal.
    
    Returns:
    A list of nodes in the order they were visited during the BFS traversal.
    """
    visited = set()
    queue = []
    bfs_order = []

    queue.append(start_node)
    visited.add(start_node)

    while queue:
        current_node = queue.pop(0)
        bfs_order.append(current_node)

        for neighbor, _ in graph.graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_order

# Example usage:
if __name__ == "__main__":
    
    # Create a graph instance and add edges
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 5)
    graph.add_edge("B", "D", 3)
    graph.add_edge("B", "E", 4)
    graph.add_edge("C", "D", 7)
    graph.add_edge("C", "F", 8)
    graph.add_edge("D", "E", 6)
    graph.add_edge("E", "F", 2)

    # Display the graph and perform BFS
    graph.display()
    
    # Perform BFS starting from node "A"
    start_node = "A"
    bfs_result = graph_bfs(graph, start_node)
    print(f"BFS starting from node {start_node}: {bfs_result}")