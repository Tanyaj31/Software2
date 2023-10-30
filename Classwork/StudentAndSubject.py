class Student:
    students = []

    def __init__(self, name):
        self.name = name
        self.courses = []
        Student.students.append(self)

    def enroll_in_course(self, course):
        self.courses.append(course)

    @classmethod
    def list_students_enrollments(cls):
        for student in cls.students:
            courses_enrolled = [course.name for course in student.courses]
            print(f"{student.name} is enrolled in courses: {', '.join(courses_enrolled)}")


class Course:
    courses = []

    def __init__(self, name):
        self.name = name
        self.students = []
        Course.courses.append(self)

    def add_student(self, student):
        self.students.append(student)

    @classmethod
    def list_students_in_course(cls):
        for course in cls.courses:
            student_names = [student.name for student in course.students]
            print(f"{course.name} has the following students: {', '.join(student_names)}")


if __name__ == "__main__":
    s1 = Student("Trung")
    s2 = Student("Amir")
    s3 = Student("Timo")

    math = Course("Mathematics")
    phy = Course("Physics")
    his = Course("History")

    s1.enroll_in_course(math)
    s2.enroll_in_course(phy)
    s3.enroll_in_course(phy)
    s3.enroll_in_course(math)
    s3.enroll_in_course(his)

    Student.list_students_enrollments()
    Course.list_students_in_course()
