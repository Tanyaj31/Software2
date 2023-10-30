class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def getData(self):
        print("The name of the student is: ", self.name)
        print("The age of the student is: ", self.age)
        print("The major of the student is: ", self.major)

# Making the objects:

s1 = Student("Tanya", 19, "IT")
s1.getData()


s2 = Student("Lara", 20, "IT")
s2.getData()

s3 = Student("Sara", 25, "IT")
s3.getData()
