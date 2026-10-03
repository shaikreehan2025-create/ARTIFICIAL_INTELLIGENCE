class VacuumCleanerAgent:
    def __init__(self, initial_location='A', room_states=None):
        self.location = initial_location
        self.room_states = room_states or {'A': 'Dirty', 'B': 'Dirty'}
        self.cost = 0

    def sense_and_act(self):
        print(f"Starting Environment State: {self.room_states}")
        print(f"Agent starts at Location: {self.location}\n")

        while 'Dirty' in self.room_states.values():
            current_status = self.room_states[self.location]
            print(f"Percept: Location = {self.location}, Status = {current_status}")

            if current_status == 'Dirty':
                print(f"Action: SUCK (Cleaning Location {self.location})")
                self.room_states[self.location] = 'Clean'
                self.cost += 1
            else:
                new_location = 'B' if self.location == 'A' else 'A'
                print(f"Action: MOVE to Location {new_location}")
                self.location = new_location
                self.cost += 1

            print(f"Updated State: {self.room_states}\n")

        print("All rooms are now CLEAN!")
        print(f"Final Environment State: {self.room_states}")
        print(f"Total Actions / Performance Cost: {self.cost}")

# Run the reflex agent
agent = VacuumCleanerAgent(initial_location='A', room_states={'A': 'Dirty', 'B': 'Dirty'})
agent.sense_and_act()