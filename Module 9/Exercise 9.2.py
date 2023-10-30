class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def show(self):
        print("The registration number is:", self.registration_number)
        print("The maximum speed is:", self.maximum_speed)
        print("The current speed is:", self.current_speed)
        print("The travelled distance is:", self.travelled_distance)

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
