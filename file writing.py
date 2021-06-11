# f = open("pews.txt", "a")
# x=f.write("pews is the best \n")
# print(x)
# f.close()

#Handles read and write both

f = open("pepe.txt", "r+")
# if i read the file like a = f.read()
# and then write something like f.write("something")
# then it'll append "something"
# if i don't read the file and straight up write something then it'll overwrite
a= f.read()
f.write("jiajiajia \n")
