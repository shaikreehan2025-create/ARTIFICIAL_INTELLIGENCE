def dfs_recursive(graph, current_node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(current_node)
    traversal_order.append(current_node)

    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)

    return traversal_order

# Define Graph as Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Graph Adjacency List:")
for node, neighbors in graph.items():
    print(f"  {node} -> {neighbors}")
print()

start_vertex = 'A'
print(f"Starting DFS traversal from node: {start_vertex}")
dfs_result = dfs_recursive(graph, start_vertex)

print("\nDepth-First Search (DFS) Traversal Order:")
print(" -> ".join(dfs_result))