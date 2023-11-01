#
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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):                             #performs operations done once per hour
        for car in self.cars:
            change_speed = random.randint(-10, 15)   #generates a random change of speed for each car
            car.accelerate(change_speed)
            car.drive(1)                            #Calls their drive method

    def print_status(self):               #prints out the current information of each car in a formatted table.
        print("{:<10} {:<15} {:<10} {:<10}".format("Reg. No.", "Max. Speed (km/h)", "Current Speed (km/h)",
                                                   "Travelled Distance (km)"))
        for car in self.cars:
            reg_no, max_speed, cur_speed, distance = car.show()
            print(f"{reg_no:<10} {max_speed:<15} {cur_speed:<10} {distance:<10}")

    def race_finished(self):    #returns True if any of the cars has reached the finish line
        return any(car.travelled_distance >= self.distance for car in self.cars)

#On creating a list of 10 car objects
cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    car = Car(registration_number, maximum_speed)
    cars.append(car)

#On creating an 8000-kilometer race called Grand Demolition Derby.
race = Race("Grand Demolition Derby", 8000, cars)

#Simulating the progressing of the race
hour = 0
while not race.race_finished():
    race.hour_passes()
    hour += 1

    #Printing current status every 10 hours and once more at the end of the race
    if hour % 10 == 0 or race.race_finished():     #race_finished method is used to check if the race has finished
        print(f"\nThe race hour is: {hour}\n")
        race.print_status()

#End of race and recognition of winners
winners = [car for car in race.cars if car.travelled_distance >= race.distance]
if winners:
    print("\nHooray!! The race is now finished! The winner(s) are:\n")
    for winner in winners:
        print(f"{winner.registration_number} - {winner.travelled_distance} km")
else:
    print("\nSorry but no cars finished this race.\n")
