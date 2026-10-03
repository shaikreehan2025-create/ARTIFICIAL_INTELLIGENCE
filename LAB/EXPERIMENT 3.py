from collections import deque

def water_jug_solver(cap1, cap2, target):
    # State: (x, y) where x is water in Jug 1, y is water in Jug 2
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        (x, y), path = queue.popleft()

        if x == target or y == target:
            return path + [((x, y), "Goal Achieved")]

        # Define production rules (next possible operations)
        operations = [
            ((cap1, y), "Fill Jug 1"),
            ((x, cap2), "Fill Jug 2"),
            ((0, y), "Empty Jug 1"),
            ((x, 0), "Empty Jug 2"),
            ((x - min(x, cap2 - y), y + min(x, cap2 - y)), "Pour Jug 1 -> Jug 2"),
            ((x + min(y, cap1 - x), y - min(y, cap1 - x)), "Pour Jug 2 -> Jug 1")
        ]

        for next_state, action in operations:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [((x, y), action)]))

    return None

# Capacities and target
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

print(f"Jug 1 Capacity: {jug1_capacity}L")
print(f"Jug 2 Capacity: {jug2_capacity}L")
print(f"Target Amount: {target_amount}L\n")

solution = water_jug_solver(jug1_capacity, jug2_capacity, target_amount)

if solution:
    print("Steps to measure target volume:")
    for step, (state, action) in enumerate(solution):
        print(f"Step {step}: Jug 1 = {state[0]}L, Jug 2 = {state[1]}L ({action})")
else:
    print("No solution possible with given capacities and target.")