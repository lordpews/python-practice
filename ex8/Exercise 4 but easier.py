num = int(input("number pls \n"))
pat = int(input("1 or  0 \n"))
if pat == 1:
    for i in range (0, num+1):
        print("*"*i)
if pat == 0:
    for i in range (num+1,0,-1):
        print("x"*i)