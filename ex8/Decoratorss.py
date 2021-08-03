# def func1():
#     print("balle balle")
# func2 = func1()
# del func1
# func2

"""def funcreturner(num):
    if num == 0:
        return print
    if num == 1:
        return sum

a = funcreturner(0)
print(a)"""
# def gooka(func):
#     func("dsadjla jkdlask jdlasd kaus")
# gooka(print)
def dec1(dunc1):
    def nowexec():
        print("executing")
        dunc1()
        print("executed")
    return nowexec
@dec1
def dolma():
    print("kaaon kaaon kaayien kaayien")

# dolma = dec1(dolma)

dolma()