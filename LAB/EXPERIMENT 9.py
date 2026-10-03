import itertools

def travelling_salesman_problem(distance_matrix, start_city=0):
    n = len(distance_matrix)
    cities = [i for i in range(n) if i != start_city]

    min_cost = float('inf')
    optimal_route = []

    # Check all permutations of intermediate cities
    for perm in itertools.permutations(cities):
        current_route = [start_city] + list(perm) + [start_city]
        current_cost = 0

        # Calculate total distance along the cycle
        for i in range(len(current_route) - 1):
            current_cost += distance_matrix[current_route[i]][current_route[i + 1]]

        if current_cost < min_cost:
            min_cost = current_cost
            optimal_route = current_route

    return optimal_route, min_cost

# Distance matrix between 4 cities (0, 1, 2, 3)
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

city_names = ['City A', 'City B', 'City C', 'City D']

print("Distance Matrix:")
print("       " + "  ".join(city_names))
for i, row in enumerate(dist_matrix):
    print(f"{city_names[i]}: {row}")
print()

print("Finding optimal Hamiltonian cycle using TSP...")
route, cost = travelling_salesman_problem(dist_matrix, start_city=0)

named_route = [city_names[idx] for idx in route]
print("\nOptimal Tour Route:")
print(" -> ".join(named_route))
print(f"Minimum Total Travel Cost: {cost}")