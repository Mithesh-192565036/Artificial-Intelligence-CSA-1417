def is_moves_left(board):
  return any(" " in row for row in board)


def evaluate(b):
  # Rows & Columns
  for i in range(3):
    if b[i][0] == b[i][1] == b[i][2] != " ":
      return 10 if b[i][0] == "O" else -10
    if b[0][i] == b[1][i] == b[2][i] != " ":
      return 10 if b[0][i] == "O" else -10
  # Diagonals
  if b[0][0] == b[1][1] == b[2][2] != " ":
    return 10 if b[0][0] == "O" else -10
  if b[0][2] == b[1][1] == b[2][0] != " ":
    return 10 if b[0][2] == "O" else -10
  return 0


def minimax(board, depth, is_max):
  score = evaluate(board)
  if score == 10 or score == -10:
    return score
  if not is_moves_left(board):
    return 0

  if is_max:  # AI turn (Maximizer)
    best = -1000
    for i in range(3):
      for j in range(3):
        if board[i][j] == " ":
          board[i][j] = "O"
          best = max(best, minimax(board, depth + 1, False))
          board[i][j] = " "
    return best
  else:  # Human turn (Minimizer)
    best = 1000
    for i in range(3):
      for j in range(3):
        if board[i][j] == " ":
          board[i][j] = "X"
          best = min(best, minimax(board, depth + 1, True))
          board[i][j] = " "
    return best


def find_best_move(board):
  best_val = -1000
  best_move = (-1, -1)
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "O"
        move_val = minimax(board, 0, False)
        board[i][j] = " "
        if move_val > best_val:
          best_move = (i, j)
          best_val = move_val
  return best_move


# Test run: AI calculates next best step for 'O'
current_board = [["X", "O", "X"], ["X", "O", " "], [" ", " ", " "]]

row, col = find_best_move(current_board)
print(f"Optimal move for AI ('O') is at Row: {row}, Column: {col}")