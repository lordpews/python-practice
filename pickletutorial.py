import pickle

# PICKLING A PYTHON LIST
# cars = ["maurti", "suzuki", "chevy", "kia"]
# fileobj = open("mycar.pkl", 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

fileobj = open("mycar.pkl",'rb')
mycar = pickle.load(fileobj)
print(mycar)


# made a list
# used 'open' to create and write file in binary format
# and we open this binary format file as fileobj
# we dump the list in the fileobj
# close the file
# mycar.pkl now contains the 'car' list


# now we open the pkl file in read binary form as file obj
# load its content in a variable
# print it lmao

