import pickle

f = open("exercise10.pkl",'rb')
list2 = pickle.load(f)
print(list2)

print(type(list2[1]))