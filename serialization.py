import pickle as pk
data = {'a':28, 'b':25, 'c':[], 'd':(12, ), 'e': {'e1': 3}}

print(pk.dumps(data))

with open("pickle.tst", "wb") as f:
    pk.dump(data, f)

with open("pickle.tst", "rb") as fich:
    data = pk.load(fich)

print(data)