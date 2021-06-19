class Employee:
    no_of_leaves = 8
    var = 10
    _protec = 100
    __privet = 22222

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

    @property
    def protec(self):
        return self._protec


class Player:
    var = 11
    no_of_games = 4

    def __init__(self, name, games):
        self.name = name
        self.games = games

    def pd(self):
        return f"name is {self.name} and games are {self.games}"


class Coolguys(Player, Employee):
    language = "opopos"

    def pl(self):
        print(self.language)


pews = Employee("piyush", 1000, "janitor")
sewp = Employee("pissu", 999, "momo wala")
ewps = Employee.from_str("ewps-320-CEO")

shum = Player("Shubham", ["badminton", "ghar ghar"])
piyush = Coolguys("puju", 2)

emp = Employee("empo", 100, "chachu")
print(emp._Employee__privet)
