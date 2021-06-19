class A:
    class_var1 = "i am a variable in class A"

    def __init__(self):
        self.var1 = "i am inside class A's contructor "
        self.class_var1 = "i am an instance variable in class A"
        self.sp = "spigot"

class B(A):
    class_var1 = "i am a variable in class b"

    def __init__(self):
        super().__init__()
        self.var1 = "i am inside class B's contructor "
        self.class_var1 = "i am an instance variable in class B"


a = A()
b = B()

print(b.class_var1)
print(b.sp)