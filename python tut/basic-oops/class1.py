class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)
# The __dict__ attribute
# Every object in Python has an attribute that is denoted by __dict__. It maps the attribute name to its value.
# This dictionary stores all the attributes defined for the object itself. Following is the syntax of using
# __dict__:object.__dict__