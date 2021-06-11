# x = 10
# y = 2929
#
#
# def sed(g):
#     x = 1000
#     """the program will check the value of x in local scope ie inside the sed()
#     if x is not defined in the local scope then it ll check the global value which in this case is x= 10"""
#     print(x)
#     """We don't have permission to modify or change global variables in local scope if i were to change('not declare')
#     the value of y(for e.g y=y+10 or y +=5 ) it would throw an error"""
#     global y
#     # ↑ if i want to change the value of a global variable i must use the global keyword like in this ↑ line('global y')
#     #if you used global keyword you cannot create a variable inside the scope after global variable you must create
#     #local variable before using global keyword
#     y = 10 + int(y) * (-3)
#     print(g, "bale bale")
#
#
# sed("jig jia")


def sewp():
    x=100
    def pews():
        global x
        x=200
# if you used global keyword you cannot create a variable inside the scope after global variable
# here we made or modified x to 200 since theres no x in local scope of pews()---('x = 200 is not a local variable')
# it made a new varibale named x in global scope with value 200 that is why is prints 200 when we print x
# outside of functions
# ie print it globally
    print("value of x before pews",x)
    pews()
    print("value of x after pews",x)

sewp()
print(x)