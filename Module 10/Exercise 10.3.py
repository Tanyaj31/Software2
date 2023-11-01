class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = self.bottom

    def go_to_floor(self, floor_no):
        print("Going to floor:", floor_no)
        if floor_no > self.current_floor:
            self.floor_up(floor_no)
        elif floor_no < self.current_floor:
            self.floor_down(floor_no)

    def floor_up(self, target_floor):
        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Current floor: {self.current_floor}")

    def floor_down(self, target_floor):
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Current floor: {self.current_floor}")

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        if elevator_num < 0 or elevator_num >= len(self.elevators):
            print(f"Invalid elevator number: {elevator_num}")
            return

        elevator = self.elevators[elevator_num]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("The fire alarm is activated. Moving all of the elevators to the bottom-most floor.\n")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)

#On creating a building with 2 elevators (ranging from the 1st to the 10th floor)
building = Building(1, 10, 2)

print("\nRunning the elevator from 0 to the 5th floor:\n")
building.run_elevator(0, 5)

print("\nRunning the elevator from 2nd to the 7th floor:\n")
building.run_elevator(1, 7)

print("\nOn activating the fire alarm:\n")
building.fire_alarm()
