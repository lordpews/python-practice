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
        params = string.split("-")
        # string.split splits the string from the argument character into a list
        # in this case it splits "ewps-320-CEO" string into a list ['ewps', '320', 'CEO']
        print(params)
        return cls(params[0], params[1], params[2])
        # return cls(*string.split("-")) one liner method of whatever we did in from_str method
pews = Employee("piyush", 1000, "janitor")
sewp = Employee("pissu", 999, "momo wala")
ewps = Employee.from_str("ewps-320-CEO")

# print(pews.printdetails())
pews.no_of_leaves = 100
print(Employee.no_of_leaves)
print(pews.no_of_leaves)

pews.change_leaves(121)

print(Employee.no_of_leaves)
print(ewps.printdetails())
