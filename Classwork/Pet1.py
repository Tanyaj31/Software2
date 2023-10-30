class Pet():
    counter=0
    def __init__(self,fname, color):
        self.fname = fname
        self.color = color
        Pet.counter+=1

    def setName(self,fname):
        self.fname=fname
        print("Name is changed: ")

    def getcolor(self):
        return self.color

    def bark(self,fname):



dog = Pet("Snowy","White")
cat = Pet("Chiko","grey")
snake = Pet("Python","yellow")

print(dog.fname,dog.color)
print(cat.fname,cat.color)
print(snake.fname,snake.color)
print("No. of objects",Pet.counter)

fish.getname() #since fish is not an object of this class so this doesn't work (exam question)
