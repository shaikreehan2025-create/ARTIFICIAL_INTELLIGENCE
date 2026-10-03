from collections import deque

# Define Goal State
GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

def get_neighbors(state):
    neighbors = []
    # Find position of empty tile (0)
    x, y = 0, 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Convert tuples to lists to allow item assignment
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

def solve_8_puzzle(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == GOAL:
            return path + [state]

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [state]))

    return None

# Initial State
initial_state = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

print("Initial State:")
for row in initial_state:
    print(row)

print("\nSolving 8-Puzzle using BFS...")
solution = solve_8_puzzle(initial_state)

if solution:
    print(f"Solution Found in {len(solution) - 1} moves!\n")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution exists.")