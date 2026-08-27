from collections import deque


def bfs(graph, start):
  visited = set([start])
  queue = deque([start])

  print("BFS Traversal:", end=" ")
  while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  print()



graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}

bfs(graph, "A")