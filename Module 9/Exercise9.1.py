class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def show(self):
        print("The registration number is:", self.registration_number)
        print(f"The maximum speed is:", self.maximum_speed,"km/h")
        print("The current speed is:", self.current_speed)
        print("The travelled distance is:", self.travelled_distance)

# Creating an object
c = Car("ABC-123", 142)
c.show()
