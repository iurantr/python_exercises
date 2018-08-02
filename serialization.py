import pickle as pk
import numpy
data4 = numpy.array([1,2,3,4])

data = {'a':28, 'b':25, 'c':[], 'd':(12, ), 'e': {'e1': 3}}

print(pk.dumps(data))

with open("pickle.tst", "wb") as f:
    #pk.dump(data, f)
    pk.dump(data4, f)

with open("pickle.tst", "rb") as fich:
    data = pk.load(fich)

print(data)

import os
print(os.getcwd())