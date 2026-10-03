import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority Queue stores: (f_score, g_score, current_node, path)
    open_queue = [(heuristics[start], 0, start, [start])]
    g_scores = {start: 0}

    while open_queue:
        f, g, current, path = heapq.heappop(open_queue)

        if current == goal:
            return path, g

        for neighbor, weight in graph.get(current, []):
            tentative_g = g + weight

            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristics.get(neighbor, 0)
                heapq.heappush(open_queue, (f_score, tentative_g, neighbor, path + [neighbor]))

    return None, float('inf')

# Weighted Graph Adjacency List: node -> list of (neighbor, edge_cost)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 12)],
    'C': [('E', 3)],
    'D': [('E', 2)],
    'E': []
}

# Heuristic estimates to goal node 'E'
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

start_node = 'A'
goal_node = 'E'

print(f"Starting A* Search from {start_node} to {goal_node}...")
optimal_path, total_cost = a_star_search(graph, heuristics, start_node, goal_node)

if optimal_path:
    print("Optimal Path Found:")
    print(" -> ".join(optimal_path))
    print(f"Total Path Cost: {total_cost}")
else:
    print("No path found to goal.")