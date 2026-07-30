class VacuumCleanerEnvironment:
    def __init__(self, location='A', status_a='Dirty', status_b='Dirty'):
        # Environment state
        self.location = location
        self.status = {'A': status_a, 'B': status_b}

    def run_agent(self):
        print(f"Initial State: Room A = {self.status['A']}, Room B = {self.status['B']}")
        print(f"Vacuum starts in Room {self.location}\n" + "-"*40)

        step = 1
        # Loop until both rooms are clean
        while self.status['A'] == 'Dirty' or self.status['B'] == 'Dirty':
            current_room = self.location
            current_status = self.status[current_room]

            print(f"Step {step}: Agent is in Room {current_room} -> Status: {current_status}")

            if current_status == 'Dirty':
                print(f"Action: SUCK (Cleaning Room {current_room})")
                self.status[current_room] = 'Clean'
            else:
                # Move to the other room if the current room is already clean
                other_room = 'B' if current_room == 'A' else 'A'
                print(f"Action: MOVE to Room {other_room}")
                self.location = other_room

            step += 1
            print("-" * 40)

        print("Both rooms are now Clean! Task complete.")

# --- Example Usage ---
# Start in Room A with both rooms dirty
env = VacuumCleanerEnvironment(location='A', status_a='Dirty', status_b='Dirty')
env.run_agent()