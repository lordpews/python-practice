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

    # classmethod() methods are bound to class rather than an object.
    # Class methods can be called by both class and object.

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


pews = Employee("piyush", 1000, "janitor")
sewp = Employee("pissu", 999, "momo wala")

# print(pews.printdetails())
pews.no_of_leaves = 100
print(Employee.no_of_leaves)
print(pews.no_of_leaves)

pews.change_leaves(121)
# here we changed class variable (no_of_leaves) using class object (pews)

print(Employee.no_of_leaves)
print(pews.no_of_leaves)
print(sewp.no_of_leaves)
