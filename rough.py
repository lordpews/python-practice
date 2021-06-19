class A:
    _proc_var = 10

    __pri_var = 20

    var = "Class A variable"


class B(A):
    # _proc_var = 12

    pass


class C(B):
    pass


c = C()
# print(c.__pri_var)

print(c._A__pri_var)
