def print_board(board):
  for row in board:
    print(" | ".join(row))
    print("-" * 9)


def check_winner(board, player):
  # Check rows, columns, and diagonals
  for i in range(3):
    if all(board[i][j] == player for j in range(3)) or all(
        board[j][i] == player for j in range(3)
    ):
      return True
  if (
      board[0][0] == board[1][1] == board[2][2] == player
      or board[0][2] == board[1][1] == board[2][0] == player
  ):
    return True
  return False


def play_game():
  board = [[" " for _ in range(3)] for _ in range(3)]
  current_player = "X"

  for turn in range(9):
    print_board(board)
    print(f"Player {current_player}'s turn.")
    row = int(input("Enter row (0, 1, 2): "))
    col = int(input("Enter column (0, 1, 2): "))

    if board[row][col] == " ":
      board[row][col] = current_player
      if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        return
      current_player = "O" if current_player == "X" else "X"
    else:
      print("Cell taken! Try again.")

  print_board(board)
  print("It's a draw!")


play_game()