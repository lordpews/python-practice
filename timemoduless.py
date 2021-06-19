import time
x = time.time()
print(x)
for i in range(0,2000):
    print("yes", end=" ")
y = time.time()
print(y)
d = float(y-x)
print(d)
# if your time difference is 0 then your pc is
# probably very fast please increase the no.
# of iterations just to see some time difference
# i increased it from 100 iterations to 2000
b = time.time()
k = 0
while k<20:
    k += 1
    print("no",end=" ")
    time.sleep(1)
    # time.sleep() is a function that delays execution for a given number of seconds.  The argument may b
    # a floating point number for subsecond precision.
g = time.time() - b
print("\n",g)
print(time.asctime())
print(time.asctime(time.localtime(time.time())))