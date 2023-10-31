class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0      #This will initialize the current_speed to 0
        self.travelled_distance = 2000  # Set the initial traveled distance to 2000 km

    def show(self):
        print("The registration number is:", self.registration_number)
        print(f"The maximum speed is:", self.maximum_speed, "km/h")
        print(f"The current speed is:", self.current_speed, "km/h")
        print(f"The travelled distance is:", self.travelled_distance, "km")

    def accelerate(self, change):
        if change < 0:
            self.current_speed = max(self.current_speed + change, 0)
        else:
            self.current_speed = min(self.current_speed + change, self.maximum_speed)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def show_speed(self):
        print("The current speed of the car is:", self.current_speed, "km/h")

# Creating an object
c = Car("ABC-123", 142)

c.current_speed = 60  # On setting the current speed to 60 km/h
c.drive(1.5)  # For driving at a constant speed for 1.5 hours
c.show()
