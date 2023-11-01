class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = self.bottom

    def go_to_floor(self, target_floor):
        if target_floor > self.top or target_floor < self.bottom:
            print(f"Invalid floor: {target_floor}. Elevator is stuck on floor {self.current_floor}")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
#Creating an elevator (h) object with a range from the bottom-most to the top-most floor
h= Elevator(1, 10)

#On taking the elevator to the 5th floor
h.go_to_floor(5)

#On returning the elevator to the bottom floor
h.go_to_floor(1)
