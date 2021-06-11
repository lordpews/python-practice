# exercise 2 Faulty exercise
"""i1 = int(input("enter the first operand: \n" ))
i2 = int(input("enter the second operand: \n" ))
op = input("enter the operator (+ = add) \n (- = sub) \n (* = mult) (/ = div)")
if i1==45:
    if i2==3:
        if op=="*":
            print("answer is 555")
        else:
            print(i1'op')
if i1==56:
        if i2==9:
            if op=="+":
                print("answer is 77")
        if i2==6:
           if op=="/":
                print("answer is 4")
if op=='+':
    print(i1+i2)
elif op=='-':
    print(i1-i2)
elif op=='*':
    print(i1*i2)
elif op=='/':
    print(i1/i2)"""

"""45*3=555,56+9=77,56/6=4"""
"""print("___________Calculator____________")
num1 = int(input("please enter the first no: \n"))
num2 = int(input("please enter the second no: \n"))
operate = ("add : +",
           "sub : -",
           "mul : *",
           "div : /",)
print(operate)
op = input()
if op == '+':
    if num1 == 56 and num2 == 9:
        print("answer is 77")
    else:
        print("answer is ", num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    if num1 == 45 and num2 == 3:
        print("answer is 555")
    else:
        print("answer is ", num1 * num2)
elif op == '/':
    if num1 == 56 and num2 == 6:
        print("answer is 4")
    else:
        print("answer is ", num1/num2)"""
while(True):
    print("___________Calculator____________")
    num1 = int(input("please enter the first no: \n"))
    num2 = int(input("please enter the second no: \n"))
    operate = ("add : +",
               "sub : -",
               "mul : *",
               "div : /",)
    print(operate)
    op = input()
    if op == '+':
        if num1 == 56 and num2 == 9:
            print("answer is 77")
        else:
            print("answer is ", num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        if num1 == 45 and num2 == 3:
            print("answer is 555")
        else:
            print("answer is ", num1 * num2)
    elif op == '/':
        if num1 == 56 and num2 == 6:
            print("answer is 4")
        else:
            print("answer is ", num1 / num2)




