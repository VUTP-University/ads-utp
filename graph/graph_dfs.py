"""
This module implements Depth-First Search (DFS) for graph traversal.
"""

from graph import Graph

def graph_dfs(graph, start_node, visited=None, dfs_order=None):
    """
    Performs Depth-First Search (DFS) on the graph starting from the specified node.
    
    Parameters:
    graph: The graph to be traversed.
    start_node: The node from which to start the DFS traversal.
    visited: A set to keep track of visited nodes.
    dfs_order: A list to record the order of nodes visited during DFS.
    
    Returns:
    A list of nodes in the order they were visited during the DFS traversal.
    """
    if visited is None:
        visited = set()
    if dfs_order is None:
        dfs_order = []

    visited.add(start_node)
    dfs_order.append(start_node)

    for neighbor, _ in graph.graph.get(start_node, []):
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited, dfs_order)

    return dfs_order


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

    # Display the graph and perform DFS
    graph.display()
    
    # Perform DFS starting from node "A"
    start_node = "A"
    dfs_result = graph_dfs(graph, start_node)
    print(f"DFS starting from node {start_node}: {dfs_result}")