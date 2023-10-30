class Person:
    def __init__(self, fname, lname, occupation, dob):
        self.fname = fname
        self.lname = lname
        self.occupation = occupation
        self.dob = dob

    def showData(self):
        print("Your first name is: ", self.fname)
        print("Your last name is: ", self.lname)
        print("Your occupation is: ", self.occupation)
        print("Your date of birth is: ", self.dob)

class Student(Person):
    def __init__(self, fname, lname, major):
        super().__init__(fname, lname, "Student", "31/05/2004")
        self.major = major

    def show(self):
        super().showData()
        print("Your major is: ", self.major)

class Teacher(Student):
    def


# Object of Student class:
s1 = Student("Tanya", "Jha", "IT")  # Initialize Student with fname, lname, occupation, and dob

s1.show()
