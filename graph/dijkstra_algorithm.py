"""
This module implements Dijkstra's algorithm to find the shortest path between two nodes in a graph.
"""

from graph import Graph


def dijkstra_algorithm(graph, start_node, end_node):
    """
    Implements Dijkstra's algorithm to find the shortest path from start_node to end_node in the graph.
    
    Parameters:
    graph: The graph on which to perform the algorithm.
    start_node: The node from which to start the pathfinding.
    end_node: The target node to reach.
    
    Returns:
    A tuple containing the shortest path as a list of nodes and the total cost of that path.
    If no path exists, returns (None, float('inf')).
    """
    import heapq

    # Priority queue to store (cost, node)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))

    # Dictionary to store the minimum cost to reach each node
    min_cost = {start_node: 0}

    # Dictionary to store the best path to each node
    best_path = {start_node: None}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        # If we reached the end node, reconstruct the path
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = best_path[current_node]
            return path[::-1], current_cost  # Return reversed path and cost

        for neighbor, weight in graph.graph.get(current_node, []):
            cost = current_cost + weight

            # If a cheaper path to neighbor is found
            if neighbor not in min_cost or cost < min_cost[neighbor]:
                min_cost[neighbor] = cost
                best_path[neighbor] = current_node
                heapq.heappush(priority_queue, (cost, neighbor))

    return None, float('inf')  # No path found


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

    # Display the graph
    graph.display()
    
    # Perform Dijkstra's algorithm from node "A" to node "F"
    start_node = "A"
    end_node = "F"
    path, cost = dijkstra_algorithm(graph, start_node, end_node)
    
    if path is not None:
        print(f"Shortest path from {start_node} to {end_node}: {path} with total cost {cost}")
    else:
        print(f"No path found from {start_node} to {end_node}")