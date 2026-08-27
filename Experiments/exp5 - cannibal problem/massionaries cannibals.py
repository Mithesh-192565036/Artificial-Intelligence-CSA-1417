from collections import deque

# State: (missionaries_left, cannibals_left, boat_position)
# boat_position: 1 for Left bank, 0 for Right bank

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    # Check bounds
    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

    # Check if cannibals outnumber missionaries on either bank
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False

    return True

def solve_missionaries_cannibals():
    start_state = (3, 3, 1) # All on left bank
    goal_state = (0, 0, 0)  # All on right bank

    # Queue stores: (current_state, path_taken)
    queue = deque([(start_state, [start_state])])
    visited = set([start_state])

    # Possible boat moves: (Missionaries, Cannibals)
    possible_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        (m_left, c_left, boat), path = queue.popleft()

        if (m_left, c_left, boat) == goal_state:
            return path

        for m_move, c_move in possible_moves:
            # If boat is on Left bank (1), subtract people; if on Right bank (0), add people
            direction = -1 if boat == 1 else 1
            
            new_m = m_left + direction * m_move
            new_c = c_left + direction * c_move
            new_boat = 1 - boat  # Switch sides (1 -> 0 or 0 -> 1)

            if is_valid(new_m, new_c) and (new_m, new_c, new_boat) not in visited:
                visited.add((new_m, new_c, new_boat))
                queue.append(((new_m, new_c, new_boat), path + [(new_m, new_c, new_boat)]))

    return None

# Run and print solution
solution = solve_missionaries_cannibals()

print("Steps to solve Missionaries & Cannibals (Left M, Left C, Boat Side):")
for step in solution:
    side = "Left" if step[2] == 1 else "Right"
    print(f"Left Bank: {step[0]} Missionaries, {step[1]} Cannibals | Boat is on: {side}")