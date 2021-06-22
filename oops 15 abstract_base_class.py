from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rect(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.l = 12
        self.b = 9

    def printarea(self):
        return self.l * self.b

# since we inherited Rect from Shape class A so we had to create a method called printarea
# if we dont override/create a new 'printarea' method on Rect it won't run
# class that has a metaclass derived from ABCMeta cannot be instantiated unless all of
# its abstract methods are overridden.


rec = Rect()
print(rec.printarea())