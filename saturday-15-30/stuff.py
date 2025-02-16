import math


class Person:

    def print_info(self):
        print("Person info")
        print("Name:", self.name)
        print("Date of birth:", self.date_of_birth)

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth


class Student(Person):
    def print_info(self):
        Person.print_info(self)
        print("Student info")
        print("Enrollment date:", self.enrollment_date)
        print("Speciality:", self.speciality)

    def __init__(self, name, date_of_birth, enrollment_date, speciality):
        Person.__init__(self, name, date_of_birth)
        self.enrollment_date = enrollment_date
        self.speciality = speciality


# arkadi = Person("Arkadi Statsenko", "17.05.2003")
# arkadi.print_info()
# print(arkadi)
# arkadi_student = Student("Arkadi Statsenko", "17.05.2003", "01.09.2022", "Computer Science")
# arkadi_student.print_info()


class Shape:
    def print_info(self):
        print("Shape info: ")
        print(f"Area: {self.area}")


class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = self.length**2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * self.radius**2


Square(5).print_info()
Circle(3).print_info()
