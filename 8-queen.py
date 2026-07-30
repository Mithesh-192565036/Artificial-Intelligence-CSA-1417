def solve_nqueens(n=8):
    cols, diag1, diag2 = set(), set(), set()
    board = [-1] * n

    def backtrack(row):
        if row == n:
            return True  # Found a valid configuration

        for col in range(n):
            d1, d2 = row - col, row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue

            # Place queen
            board[row] = col
            cols.add(col); diag1.add(d1); diag2.add(d2)

            if backtrack(row + 1):
                return True

            # Backtrack
            cols.remove(col); diag1.remove(d1); diag2.remove(d2)
            
        return False

    # FIX: Call backtrack(0) instead of solve_nqueens(0)
    if backtrack(0):
        print(f"{n}-Queen Solution (Row index -> Column index):")
        print(board)
        print("\nVisual Board:")
        for row in board:
            print(". " * row + "Q " + ". " * (n - row - 1))
    else:
        print("No solution found.")

# Run the function
solve_nqueens()