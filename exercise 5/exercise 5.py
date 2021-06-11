def getdate():
    import datetime
    return datetime.datetime.now()


def read_data():
    f = open(x)
    a = f.read()
    print(a)
    f.close()


def log_data():
    dt = str(getdate())
    f = open(x, "a")
    inp = input("enter your data")
    f.write(dt)
    f.write("\n")
    f.write(inp)
    f.write("\n")
    f.close()


print("__welcome to our health management system__")
r = int(input("chose your client\n"
              "1 for PEWS1 \n"
              "2 for PEWS2 \n"
              "3 for PEWS3 \n"))

if r == 1:
    req = int(input("do you want to log data or read \n 1 : LOG 2: READ"))
    if req == 1:
        req2 = int(input("1: log exercise \n2: log food"))
        if req2 == 1:
            x = "p1ex.txt"
            log_data()

        if req2 == 2:
            x = "p1fd.txt"
            log_data()
    if req == 2:
        req2 = int(input("1: read exercise \n2: read food"))
        if req2 == 1:
            x = "p1ex.txt"
            read_data()

        if req2 == 2:
            x = "p1fd.txt"
            read_data()

if r == 2:
    req = int(input("do you want to log data or read \n 1 : LOG 2: READ"))
    if req == 1:
        req2 = int(input("1: log exercise \n2: log food"))
        if req2 == 1:
            x = "p2ex.txt"
            log_data()

        if req2 == 2:
            x = "p2fd.txt"
            log_data()
    if req == 2:
        req2 = int(input("1: read exercise \n2: read food"))
        if req2 == 1:
            x = "p2ex.txt"
            read_data()

        if req2 == 2:
            x = "p2fd.txt"
            read_data()

if r == 3:
    req = int(input("do you want to log data or read \n 1 : LOG 2: READ"))
    if req == 1:
        req2 = int(input("1: log exercise \n2: log food"))
        if req2 == 1:
            x = "p3ex.txt"
            log_data()

        if req2 == 2:
            x = "p3fd.txt"
            log_data()
    if req == 2:
        req2 = int(input("1: read exercise \n2: read food"))
        if req2 == 1:
            x = "p3ex.txt"
            read_data()

        if req2 == 2:
            x = "p3fd.txt"
            read_data()
