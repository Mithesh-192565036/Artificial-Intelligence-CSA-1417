from itertools import permutations


def travelling_salesman(matrix, start=0):
  num_cities = len(matrix)
  cities = [i for i in range(num_cities) if i != start]

  min_cost = float("inf")
  best_path = []

  # Test all possible city routes
  for perm in permutations(cities):
    current_cost = 0
    current_path = [start] + list(perm) + [start]

    # Calculate distance for the current route
    for i in range(len(current_path) - 1):
      current_cost += matrix[current_path[i]][current_path[i + 1]]

    if current_cost < min_cost:
      min_cost = current_cost
      best_path = current_path

  return min_cost, best_path


cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]

cost, path = travelling_salesman(cost_matrix)
print("Minimum Cost:", cost)
print("Best Route:", " -> ".join(map(str, path)))