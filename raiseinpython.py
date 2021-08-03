# a =  input("enter your name?")
# b =  int(input("kitna pasiee?"))
# if b == 0:
#     raise ZeroDivisionError("b = 0  lmao")
# if a.isnumeric()==True:
#     raise Exception("numbers are not allowed")
# print(f"hello {a}")

c = input("enter your name again")
try:
    print(a)
except Exception as e:
    if c == "pews":
        raise ValueError("please dont")
    print("exception handled bawa")