# Self & __init__() (Constructors)
# def read_number(self):
#     print(self.num)
# def __init__(self):
#   body of the constructor
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
"""


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}.My Salary is {self.salary} and role is {self.role}"


DK= Employee("Dhanesh", 255, "Instructor")
Sk= Employee("SK",486,"Student")
# Dk.name = "Dhanesh"
# DK.salary = 455
# DK.role = "Instructor"

# Sk.name = "SK"
# SK.salary = 4554
# SK.role = "Student"

print(Sk.printdetails())
