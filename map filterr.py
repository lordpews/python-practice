# num = ["2", "32", "3232", "12"]
# num = list(map(int, num))
# # map is used to apply a function or lambda function to each element of an iterable
# # S Y N T A X
# # map(function, iterable)
# # map() function returns a map object(which is an iterator) of the results
# # after applying the given function to each item of a given iterable (list, tuple etc.)
# print(num)

"""for i in range(len(num)):
    num[i] = int(num[i])

num[2] = num[2] + 1
print(num[2])
"""
# num= list(map(int, num)) (line 2)
# here we use map function to make all string elements of list 'num' an integer
# this map function returned a map object which we turn into a list by using list()

"""lisq = [2,3,4,5]

opog = list(map(lambda x: x*x , lisq))
print(opog)
"""
def sq(a):
    return a*a
def cb(a):
    return a*a*a
fogi = [sq,cb]
num = [2,3,4,5,6]
for i in range(0,5):
    val = list(map(lambda x:x(i),fogi))
    print(val)