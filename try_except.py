print("enter num1")
num1 = (input())
print("enter num2")
num2 = (input())
try:
    print("the sum is", int(num2) + int(num1))
except Exception as e:
    print(e)

print("this line is important")
