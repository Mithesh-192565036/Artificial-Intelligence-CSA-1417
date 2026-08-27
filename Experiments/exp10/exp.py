def is_valid(region, color, assignment, neighbors):
  # Ensure adjacent regions do not have the same color
  for neighbor in neighbors[region]:
    if neighbor in assignment and assignment[neighbor] == color:
      return False
  return True


def map_coloring(regions, colors, neighbors, assignment={}):
  if len(assignment) == len(regions):
    return assignment  # All regions are colored

  # Select the next uncolored region
  uncolored = [r for r in regions if r not in assignment][0]

  for color in colors:
    if is_valid(uncolored, color, assignment, neighbors):
      assignment[uncolored] = color
      result = map_coloring(regions, colors, neighbors, assignment)
      if result:
        return result
      del assignment[uncolored]  # Backtrack

  return None


# Regions (e.g., Australian territory map)
regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
colors = ["Red", "Green", "Blue"]

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}

solution = map_coloring(regions, colors, neighbors)
for region, color in solution.items():
  print(f"{region}: {color}")