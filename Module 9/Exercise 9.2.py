class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0       #This will initialize the current_speed to 0
        self.travelled_distance = 0     #This will initialize the travelled_distance to 0

    def show(self):
        print("The registration number is:", self.registration_number)
        print(f"The maximum speed is:", self.maximum_speed, "km/h")
        print("The current speed is:", self.current_speed)
        print("The travelled distance is:", self.travelled_distance)

    def accelerate(self, change):
        if change < 0:
            # Now, on implementing the braking logic (speed can't be less than 0)
            self.current_speed = max(self.current_speed + change, 0)
        else:
            # Now, on implementing the acceleration logic (speed can't be more than 142km/h)
            self.current_speed = min(self.current_speed + change, self.maximum_speed)

    def show_speed(self):
        print(f"The current speed of the car is:", self.current_speed, "km/h")

# Creating an object
c = Car("ABC-123", 142)

c.accelerate(30)
c.show_speed()

c.accelerate(70)
c.show_speed()

c.accelerate(50)    #The speed can't reach 150 km/h as it has to be below the maximum speed (142 km/h)
c.show_speed()       #So the output will be 142 km/h

c.accelerate(-200)   #on applying the emergency brake by forcing a -200 km/h change on the speed
c.show_speed()        #so the output will be 0 as it can't be a negative value.
