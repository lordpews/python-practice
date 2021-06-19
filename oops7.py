class Employee:
    no_of_leaves = 8

    def __init__(self, xname, xsalary, xrole):
        self.name = xname
        self.salary = xsalary
        self.role = xrole

    def printdetails(self):
        return f"name is {self.name} \n" \
               f"salary is {self.salary} \n" \
               f"role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def prg(string):
        print("this is good and " + string)


class Programmer(Employee):
    def __init__(self, xname, xsalary, xrole, *lgs):
        self.name = xname
        self.salary = xsalary
        self.role = xrole
        self.langgs = lgs

    def printprog(self):
        return f"name is {self.name}, salary is {self.salary} ,role is {self.role}" \
               f"\n languages is {self.langgs}"


pews = Employee("piyush", 1000, "janitor")
sewp = Employee("pissu", 999, "momo wala")
ewps = Employee.from_str("ewps-320-CEO")

# pews.no_of_leaves = 100
# print(Employee.no_of_leaves)
# print(pews.no_of_leaves)
#
# pews.change_leaves(121)
#
# print(Employee.no_of_leaves)
# print(ewps.printdetails())
joos = Programmer("jus", 10002, "jr programmer", "java")
poos = Programmer("puss", 323232, "sr programmer", "pyhton","pyhton","pyhton","pyhton")
print(joos.printdetails())

print(poos.printprog())
