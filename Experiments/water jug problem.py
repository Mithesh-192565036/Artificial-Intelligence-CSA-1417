from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    # Queue stores (jug_a_water, jug_b_water, path_taken)
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        a, b, path = queue.popleft()

        # If we reached the target in Jug A, return the path
        if a == target:
            return path + [(a, b)]

        # Skip if we have already seen this combination of water levels
        if (a, b) in visited:
            continue
        visited.add((a, b))

        # Current state added to current path
        current_path = path + [(a, b)]

        # Generate all possible next moves:
        moves = [
            (capacity_a, b),  # Fill Jug A
            (a, capacity_b),  # Fill Jug B
            (0, b),           # Empty Jug A
            (a, 0),           # Empty Jug B
            # Pour A into B until B is full or A is empty
            (a - min(a, capacity_b - b), b + min(a, capacity_b - b)),
            # Pour B into A until A is full or B is empty
            (a + min(b, capacity_a - a), b - min(b, capacity_a - a))
        ]

        for next_a, next_b in moves:
            queue.append((next_a, next_b, current_path))

    return None

# --- Example Usage ---
# Jug A: 4L, Jug B: 3L, Target: 2L
steps = water_jug_problem(4, 3, 2)

print("Steps to solve the Water Jug Problem (Jug A, Jug B):")
for step in steps:
    print(f"Jug A: {step[0]}L, Jug B: {step[1]}L")