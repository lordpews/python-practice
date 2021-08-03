# After saving Iris. data file, parse it using the split() function or using a new line approach.
# The method of parsing is up to you.
# The main task is to get the list of lists that you will pickle.
# And after creating the pickle, write a code to read it. For downloading the Iris dataset, use the request module.
import pickle

import requests

req = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
r = req.text
print(type(r))

list1 = r.split("\n")
lista = [[i] for i in list1]
print(lista)

data_obj = open("exercise10.pkl", 'wb')
pickle.dump(lista, data_obj)
data_obj.close()
