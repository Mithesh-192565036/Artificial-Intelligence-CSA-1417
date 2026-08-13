import itertools

def solve_cryptarithmetic():
    # Equation: SEND + MORE = MONEY
    # Unique letters involved: S, E, N, D, M, O, R, Y (8 letters)
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    # Try every possible combination of 8 unique digits
    for perm in itertools.permutations(digits, len(letters)):
        # Map each letter to a digit from the current combination
        mapping = dict(zip(letters, perm))

        # First letters of words cannot be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Convert letter words into numbers
        send = mapping['S']*1000 + mapping['E']*100 + mapping['N']*10 + mapping['D']
        more = mapping['M']*1000 + mapping['O']*100 + mapping['R']*10 + mapping['E']
        money = mapping['M']*10000 + mapping['O']*1000 + mapping['N']*100 + mapping['E']*10 + mapping['Y']

        # Check if the equation holds true
        if send + more == money:
            print("Solution Found!")
            print(f"  {send}  (SEND)")
            print(f"+ {more}  (MORE)")
            print("-------")
            print(f" {money}  (MONEY)\n")
            print("Letter Mapping:")
            for letter, digit in mapping.items():
                print(f"{letter} = {digit}")
            return

# Run the solver
solve_cryptarithmetic()