class car:
    def __init__(self): # whenever we create an object __init__ is automatically called
        # hence it calls the __updatesoftware()
        self.__updatesoftware()

    def drive(self):
        print("driving")

    def __updatesoftware(self):  # __ means that its a private method and it cant be called outside the class
        print("updating software")


blackcar = car()
blackcar.drive()
blackcar.__updatesoftware()
# this 👆 line will give the following error because it cant be directly accessed
# AttributeError: 'car' object has no attribute '__updatesoftware'
# it couldnt be called outside the class because it was a private method so we had to call it inside the class
# with __init__
