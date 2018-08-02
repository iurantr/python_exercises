from functools import reduce

print(bool(reduce(lambda x, y: x and y, [0, 1, 3])))
print(all([0, 1, 3]))
print(any([0, 1, 3]))

print([bool(x) for x in [0, 1, 3]])
print(bool([0, 1, 3]))
