import heapq

# Manhattan Distance heuristic
def heuristic(state):
    distance = 0
    for i, val in enumerate(state):
        if val != 0:  # Skip blank space
            target_r, target_c = val // 3, val % 3
            curr_r, curr_c = i // 3, i % 3
            distance += abs(target_r - curr_r) + abs(target_c - curr_c)
    return distance

def solve_8_puzzle(start, goal=(0, 1, 2, 3, 4, 5, 6, 7, 8)):
    # Priority Queue stores: (f_score, g_score, state, path)
    pq = [(heuristic(start), 0, start, [])]
    visited = {start}

    while pq:
        _, g, current, path = heapq.heappop(pq)
        
        if current == goal:
            return path + [current]

        zero_idx = current.index(0)
        r, c = zero_idx // 3, zero_idx % 3

        # Possible moves: Up, Down, Left, Right
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_idx = nr * 3 + nc
                
                # Swap blank tile with adjacent tile
                state_list = list(current)
                state_list[zero_idx], state_list[new_idx] = state_list[new_idx], state_list[zero_idx]
                neighbor = tuple(state_list)

                if neighbor not in visited:
                    visited.add(neighbor)
                    heapq.heappush(pq, (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [current]))

    return None

# Printable board helper
def print_board(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[i:i+3]))
    print()

# Example Usage:
start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
solution = solve_8_puzzle(start_state)

if solution:
    print(f"Solved in {len(solution) - 1} moves:\n")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        print_board(state)
else:
    print("No solution exists for this configuration.")