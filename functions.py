"""def myfunc():
    a = int(input("enter the input a \n"))
    b = int(input("enter the input b \n"))
    c = int(input("enter the input c \n"))
    print(a+b-c)"""
"""myfunc()
def func1(a,b):
    print("sum is ", a+b)
func1(4,5)
"""


def funcfuuc(a, b):
    """this is a function"""
    avg = (a + b) / 2
    return avg


ga = funcfuuc(20, 14)

print(ga)
"""
how the function cycle works taking funcfuuc example
the program ignores the defining part of function 'funfuuc'
it straight up goes to the ga= funcfuuc (20,14) part
then its sees that funcfuuc(x,y) syntax means theres a function with two arguments
then it goes to the function part puts the value of x and y in a and b in this case its 10 and 14
performs the defined function of adding them and then dividing them by 2
and 'return' the value of avg in funcfuuc
so if you perform funcfuuc on 2 values itll return the result and store them in ga
and the you print ga ;)
"""
print(funcfuuc.__doc__)
