def alpha_beta(depth, node_index, is_maximizing, values, alpha, beta):
  # Terminal node reached (leaf of the game tree)
  if depth == 3:
    return values[node_index]

  if is_maximizing:
    best = float('-inf')
    for i in range(2):  # 2 branches per node
      val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
      best = max(best, val)
      alpha = max(alpha, best)

      # Prune branch
      if beta <= alpha:
        break
    return best

  else:
    best = float('inf')
    for i in range(2):
      val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
      best = min(best, val)
      beta = min(beta, best)

      # Prune branch
      if beta <= alpha:
        break
    return best


# 8 leaf node values for a binary tree of depth 3
leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]

optimal_value = alpha_beta(0, 0, True, leaf_values, float('-inf'), float('inf'))
print("Optimal value calculated by Alpha-Beta Pruning:", optimal_value)