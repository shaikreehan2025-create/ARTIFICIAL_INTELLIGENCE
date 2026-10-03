from collections import deque

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    visited.append(start_node)
    traversal_order = []

    print(f"Starting BFS traversal from node: {start_node}")

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

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

bfs_result = bfs(graph, 'A')
print("\nBreadth-First Search (BFS) Traversal Order:")
print(" -> ".join(bfs_result))