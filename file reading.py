x = open("pews.txt", "rt")

"""k = (x.read(8))
print(k)
# here it reads and then dumps first 8 characters of pews.txt file into the k variable
k = (x.read(9))
# since it read and dumped the first 8 characters into the the k variable now it'll read the next 9 characters
print(k)"""
"""for d in k:
    print(d)"""
# print(x.readline()) itll also read and dump the data like x.read function
# print(x.readline())
# print(x.readline())
k=(x.readlines())
print(k)
x.close()
