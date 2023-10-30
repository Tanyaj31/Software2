class Car:
 def __init__(self,register_number,maximum_speed):
  self.register_number=register_number
  self.maximum_speed=maximum_speed
  self.current_speed=0
  self.travel_distance=0

 def show(self):
  print("Register Number is  :",self.register_number)
  print("Maximum Speed  is   :",self.maximum_speed)
  print("Current Speed is    :",self.current_speed)
  print("Travel Distance  is :",self.travel_distance)


class NewCar(Car):
  def __init__(self):
   super().__init__("ABC-123",142)

  def accerelate(self,speed):
   if(speed<0):
    print("speed can not zero")
   else:
    self.current_speed=self.current_speed+speed

  def show_speed(self):
    print("Current speed of Car is :",self.current_speed)

  def brake_method(self,bspeed):
    self.current_speed=self.current_speed+bspeed

  def drive_method(self,hrs):
    self.travel_distance=2000
    self.current_speed=60
    self.travel_distance=self.travel_distance+(hrs*60)
    print("Travel Distance is ",self.travel_distance)


#creating object
c=NewCar()


car=["BMW","AUDI","NANO","TESLA","TATA","TAVERA","CRETA","Nexa","I10","I20"]

reg_no=["ABC-1","ABC-2","ABC-3","ABC-4","ABC-5","ABC-6","ABC-7","ABC-8","ABC-9","ABC-10"]

max_speed=[100,110,120,130,140,150,160,170,180,190]

print("\nChange Speed  by 10")
for ms in max_speed:
 c.accerelate(ms-10)
 c.show_speed()


print("\nChange Speed  by 15")
for ms in max_speed:
 c.accerelate(ms+15)
 c.show_speed()


c.drive_method(1)