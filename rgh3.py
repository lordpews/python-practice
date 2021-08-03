import pickle
fileobj=open('irisData.pkl','rb')

data=pickle.load(fileobj)

print(data)