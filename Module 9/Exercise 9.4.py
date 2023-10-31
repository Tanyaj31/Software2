import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0        #This will initialize the current_speed to 0
        self.travelled_distance = 0   #This will initialize the travelled_distance to 0

    def accelerate(self, change):
        if change < 0:
            self.current_speed = max(self.current_speed + change, 0)
        else:
            self.current_speed = min(self.current_speed + change, self.maximum_speed)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def show(self):
        return [self.registration_number, self.maximum_speed, self.current_speed, self.travelled_distance]


# On creating a list of 10 car objects
cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    car = Car(registration_number, maximum_speed)
    cars.append(car)

#The race until one car travels at least 10,000 km
while True:
    for car in cars:
        change_speed = random.randint(-10, 15)
        car.accelerate(change_speed)
        car.drive(1)

    if any(car.travelled_distance >= 10000 for car in cars):
        break

#Now, on printing the properties of each car in a table format
print("{:<10} {:<15} {:<10} {:<10}".format("Reg. No.", "Max. Speed (km/h)", "Current Speed (km/h)",
                                           "Travelled Distance (km)"))
for car in cars:
    reg_no, max_speed, cur_speed, distance = car.show()
    print(f"{reg_no:<10} {max_speed:<15} {cur_speed:<10} {distance:<10}")
