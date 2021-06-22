class Employee:
    no_of_leaves = 8

    def __init__(self, xname, xsalary, xrole,xskill):
        self.name = xname
        self.salary = xsalary
        self.role = xrole
        self.skill = xskill

    def printdetails(self):
        return f"name is {self.name} \n" \
               f"salary is {self.salary} \n" \
               f"role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return f"{self.name}, {self.salary}, {self.role}, {self.skill}"
    def __str__(self):
        return f"from str \n {self.name}, {self.salary}, {self.role} , {self.skill}"
    def __sub__(self, other):
        return self.skill - other.skill
    def __mul__(self, other):
        return self.skill * other.skill
    def __truediv__(self, other):
        return self.skill / other.skill


pews = Employee("piyush", 100, "janitor",100)
pews2 = Employee("piyush2", 120, "jr. janitor",10)

print(pews)
print(pews - pews2)
print(pews * pews2)
print(pews/pews2)