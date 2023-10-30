class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def show(self):
        print("Register Number is:", self.registration_number)
        print("Maximum Speed is:", self.maximum_speed)
        print("Current Speed is:", self.current_speed)
        print("Travel Distance is:", self.travelled_distance)

class NewCar(Car):
    def __init__(self):
        super().__init__("ABC-123", 142)

    def accelerate(self, speed):
        if speed < 0:
            print("Speed cannot be negative.")
        else:
            self.current_speed = min(self.current_speed + speed, self.maximum_speed)
            self.current_speed = max(self.current_speed, 0)

    def show_speed(self):
        print("Current speed of Car is:", self.current_speed)

    def brake_method(self, bspeed):
        self.accelerate(bspeed)

    def drive(self, hrs):
        if self.current_speed > 0:
            additional_distance = self.current_speed * hrs
            self.travelled_distance += additional_distance
        else:
            print("The car is not moving, so no distance is added.")

# Creating an object
c = NewCar()

c.accelerate(30)
c.show_speed()

c.accelerate(70)
c.show_speed()

c.accelerate(50)
c.show_speed()

c.brake_method(-200)
c.show_speed()

c.drive(1.5)
c.show_speed()
