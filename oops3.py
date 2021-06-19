class Employee:
    no_of_leaves = 8
    def __init__(self,xname,xsalary,xrole):
        self.name = xname
        self.salary = xsalary
        self.role = xrole

    def printdetails(self):
        return f"name is {self.name} \n" \
            f"salary is {self.salary} \n" \
            f"role is {self.role}"

pews = Employee("piyush",1000,"janitor")
sewp = Employee("pissu",999,"momo wala")

"""pews.name = "pews"
pews.salary = 455
pews.role = "momo wala"

sewp.name = "sewp"
sewp.salary = 4554
sewp.role = "janitor"
"""
print(Employee.no_of_leaves)
# print(Employee.__dict__)
Employee.no_of_leaves = 9
# print(Employee.__dict__)
print(Employee.no_of_leaves)

print(pews.printdetails())
