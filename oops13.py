class A:
    def meth(self):
        print("method from class a")


class B(A):
    def meth(self):
        print("method from class b")


class C(A):
    def meth(self):
        print("method from class c")


class D(B, C):
    def meth(self):
        print("method from class d")


a = A()
b = B()
c = C()
d = D()

print(d.meth())
