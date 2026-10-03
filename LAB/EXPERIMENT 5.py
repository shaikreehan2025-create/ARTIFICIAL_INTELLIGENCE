from collections import deque

def is_valid(m, c):
    # Check bounds
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    # Check left bank constraint
    if m > 0 and m < c:
        return False
    # Check right bank constraint
    rm, rc = 3 - m, 3 - c
    if rm > 0 and rm < rc:
        return False
    return True

def solve_missionaries_cannibals():
    # State: (M, C, B) on left bank. B=1 left bank, B=0 right bank
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = {start}

    # Possible boat passengers: (M, C)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        (m, c, b), path = queue.popleft()

        if (m, c, b) == goal:
            return path + [((m, c, b), "All safely reached destination")]

        for dm, dc in moves:
            if b == 1:  # Crossing from left to right bank
                nm, nc, nb = m - dm, c - dc, 0
                action = f"Send {dm} Missionary(ies) & {dc} Cannibal(s) to Right"
            else:       # Returning from right to left bank
                nm, nc, nb = m + dm, c + dc, 1
                action = f"Return {dm} Missionary(ies) & {dc} Cannibal(s) to Left"

            if is_valid(nm, nc) and (nm, nc, nb) not in visited:
                visited.add((nm, nc, nb))
                queue.append(((nm, nc, nb), path + [((m, c, b), action)]))

    return None

print("Solving Missionaries and Cannibals Problem using BFS...\n")
solution = solve_missionaries_cannibals()

if solution:
    print("Solution Steps:")
    for step, (state, action) in enumerate(solution):
        m, c, b = state
        rm, rc = 3 - m, 3 - c
        print(f"Step {step:2d}: Left=[{m}M, {c}C] | Right=[{rm}M, {rc}C] | {action}")
else:
    print("No solution found.")