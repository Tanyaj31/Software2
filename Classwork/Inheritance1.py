class Animal:
 def __init__(self,name):
  self.name=name

 def speak(self):
  pass

 def print_me(self):
  print(f"{self.name}")

class Dog(Animal):
 def speak(self):
  print("Wau wau!!")

myDog= Dog("Snowy")
myDog.speak()


myAnimal=[]
myAnimal.append(Animal("dog"))
myAnimal.append(Animal("cat"))
myAnimal.append(Animal("fish"))

for animal in myAnimal:
 animal.print_me()

class Cat(Animal):
 def speak(self):
  print("mau mau!")

myCat = Cat("Chiko")
myCat.speak()
