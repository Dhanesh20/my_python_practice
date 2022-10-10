class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}.My Salary is {self.salary} and role is {self.role}"
##IMP
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
##

DK= Employee("Dhanesh", 255, "Instructor")
Sk= Employee("SK",486,"Student")
DK.change_leaves(22)
print(DK.no_of_leaves)