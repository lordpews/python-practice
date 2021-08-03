import os

# print(dir(os))
print(os.getcwd())  # shows the current directory

# example   if you want to open a file as f= open("file.txt")
# and you do not provide the exact location it ll check the requested file in your current directory ie the directory
# where program is currently located that's what 'os.cwd()' will print or return or display

"""os.chdir("C://")"""  # changes the current working directory

# print(os.getcwd())

x = (os.listdir())  # Returns a list of  all the files or folders present in current working directory

# in this case the current working directory is C://
"""os.mkdir("this")"""  # creates a directory

os.chdir("C:/Users/piyush thakur/PycharmProjects")

"""os.makedirs("lol/lmao")"""  # used make a directory inside a directory

print(os.getcwd())
# os.makedirs("lol")

"""os.rename("pepe.txt", "pepee.txt")"""  # changes name of a file

# syntax os.rename("oldname","newname")

print(os.environ.get('path'))

print(os.path.join("C://", "pepee.txt"))

"""
It joins one or more path components.
We can join the paths by simply using a + sign,
but the benefit of using this function is that we do not have to worry about extra slashes between the components.
So less accuracy still provides us with the same result.
"""

print(os.path.exists("C:/Users/piyush thakur/PycharmProjects"))

# checks whether a 'PATH' exists or not if it exists it'll return  true else it'll return falls

print(os.path.isfile("jila2.py"))

# checks whether a 'FILE' exists or not if it exists it'll return  true else it'll return falls

print(os.path.isdir("exercise 5"))

# checks whether a 'DIRECTORY' exists or not if it exists it'll return  true else it'll return falls
print(x[0])
print(type(x[0]))