import pickle

b = ['123','alknf']
a = open("a.txt","rb")
c = pickle.load(a)
print(c)
a.close()