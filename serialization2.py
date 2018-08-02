import json

import numpy
data4 = numpy.ndarray([1,2,3,4]) # doesn't work with json serialization

data2 = {'a':28, 'b':25, 'c':[], 'd':(12, ), 'e': {'e1': 3}}
data3 = []

with open("json.tst", "w") as ficher_ser:
    json.dump(data2, ficher_ser)

with open("json.tst", "r") as ficher_deser:
    data = json.load(ficher_deser)
print(data)

