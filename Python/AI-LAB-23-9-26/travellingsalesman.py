import math

def solve_tsp_held_karp(distance_matrix):
    n = len(distance_matrix)
    memo = {}

    def get_min_cost(mask, current_city):
        # Base case: All cities visited, return cost to return to starting city (0)
        if mask == (1 << n) - 1:
            return distance_matrix[current_city][0], [0]

        state = (mask, current_city)
        if state in memo:
            return memo[state]

        min_cost = math.inf
        best_path = []

        for next_city in range(n):
            # If city hasn't been visited yet
            if not (mask & (1 << next_city)):
                new_cost, path = get_min_cost(mask | (1 << next_city), next_city)
                total_cost = distance_matrix[current_city][next_city] + new_cost

                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = [next_city] + path

        memo[state] = (min_cost, best_path)
        return memo[state]

    # Start at city 0, initial mask has only bit 0 set (1)
    min_cost, path = get_min_cost(1, 0)
    full_path = [0] + path
    return min_cost, full_path

# Example: 4 cities distance matrix
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = solve_tsp_held_karp(dist)
print(f"Optimal Cost: {cost}")
print(f"Optimal Path: {' -> '.join(map(str, path))}")
# Output: Optimal Cost: 80, Path: 0 -> 1 -> 3 -> 2 -> 0