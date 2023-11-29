class Car:
    def __init__(self, registration_number, maximum_speed):  #initializing the basic properties for the car class
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        #seeing if the current speed is based on acceleration/deceleration
        if change < 0:
            self.current_speed = max(self.current_speed + change, 0)
        else:
            self.current_speed = min(self.current_speed + change, self.maximum_speed)

    def drive(self, hours):
        dist_covered = self.current_speed * hours     #calculating the distance covered during the given time
        self.travelled_distance += dist_covered       #to find the total travelled distance
        return dist_covered                           #returning the value of the distance covered

    def show_max_speed(self):            #printing the maximum speed of the car
        print(f"The maximum speed of the car is {self.maximum_speed} km/h")


class ElectricCar(Car):                 #ElectricCar subclass inherits from Car base class
    def __init__(self, registration_number, maximum_speed, battery_capacity):     #initializing
        super().__init__(registration_number, maximum_speed)      #to call Car class's data members
        self.battery_capacity = battery_capacity      #setting the property for ElectricCar class


class GasolineCar(Car):             #GasolineCar subclass inherits from Car base class
    def __init__(self, registration_number, maximum_speed, tank_volume):      #initializing
        super().__init__(registration_number, maximum_speed)        #to call Car class's data members
        self.tank_volume = tank_volume           #setting the property for GasolineCar class


#main program
selected_ElectricCar_speed = 100
selected_GasolineCar_speed = 90
given_time = 3

#objects of ElectricCar and GasolineCar classes
electric_car_1 = ElectricCar("ABC-15", 180, 52.5)
gasoline_car_1 = GasolineCar("ACD-123", 165, 32.3)

#accelerating both cars to given speeds
electric_car_1.accelerate(selected_ElectricCar_speed)
gasoline_car_1.accelerate(selected_GasolineCar_speed)

#driving both cars for the given time and printing results
electric_distance = electric_car_1.drive(given_time)
print(f"The distance travelled for Electric Car is {electric_distance:.2f} km.")

gasoline_distance = gasoline_car_1.drive(given_time)
print(f"The distance travelled for Gasoline Car is {gasoline_distance:.2f} km.")
