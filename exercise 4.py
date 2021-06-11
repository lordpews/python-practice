"""

just check exercise 4 but easier ;)

"""
print("astrologer's stars")
s = int(input("enter the holy integer"))


def boole(x):
    if x.lower() == "true":
        x = True
        print("ascending pattern")
        return x
    elif x.lower() == "false":
        x = False
        print("descending pattern")
        return x


# this boole() function is almost useless i made it for fun could be simplified and doesnt do
# much in functioning of this program.

p = input("enter true or false")
boole(p)

if boole(p) == True:
    for i in range(1, s + 1):
        for j in range(1, i + 1):
            print("*", end=" ")  # end=" " makes the next print() print in the same line instead of new line
        print()
else:
    for i in range(s + 1, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
#   super accurate functioning of above program
#   starting with the true part
#   for i in range(1, s + 1) makes a local variable 'i' and its value is 1 initially with 'range' function its
#   value will keep on increasing by +1 from initial value 1 to s+1
#   first for loop will run until value of i reaches s+1
#   within first loop, second loop  for j in range(1, i + 1): will run multiple times
#   for example when value of i is 1 then for 1 loop in first loop (for i in range(1, s + 1):), second loop will run
#   2 times beacause  second loops runs for range (1,i+1) so when value of i is 1 it runs for range (1, 2)
#
