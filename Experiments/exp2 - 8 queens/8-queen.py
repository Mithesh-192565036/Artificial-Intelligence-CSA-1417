def solve_nqueens(n=8, start_row=1, start_col=1):
    # Boundary check for the custom starting position
    if not (0 <= start_row < n and 0 <= start_col < n):
        print(f"Error: Starting position ({start_row}, {start_col}) is out of bounds for a {n}x{n} board.")
        return

    cols, diag1, diag2 = set(), set(), set()
    board = [-1] * n

    # 1. Pre-place the queen at the designated starting position
    board[start_row] = start_col
    cols.add(start_col)
    diag1.add(start_row - start_col)
    diag2.add(start_row + start_col)

    def backtrack(row):
        # Base case: All rows processed successfully
        if row == n:
            return True

        # Skip the row if we already fixed the starting queen there
        if row == start_row:
            return backtrack(row + 1)

        for col in range(n):
            d1, d2 = row - col, row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue

            # Place queen
            board[row] = col
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)

            if backtrack(row + 1):
                return True

            # Backtrack
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)

        return False

    # Start backtracking from row 0
    if backtrack(0):
        print(f"{n}-Queen Solution with initial Queen at ({start_row}, {start_col}):")
        print("Row index -> Column index:", board)
        print("\nVisual Board:")
        for row in board:
            print(". " * row + "Q " + ". " * (n - row - 1))
    else:
        print(f"No solution exists with a Queen starting at ({start_row}, {start_col}).")

# Example Usage:
# Try placing the first queen at Row 2, Column 4
solve_nqueens(n=8, start_row=2, start_col=4)