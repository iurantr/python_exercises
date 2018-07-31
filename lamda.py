def f(x):
    return x ** 2


g = lambda x: x ** 2
print(f)
print(g)
print(f(3) == g(3))

# Faire une concatenation par ':'
g = lambda l: ":".join(l)
list_chars = ["Ouriel", "Iurii", "Marie", "Kenza"]
print(g(list_chars))

# Another possibility (unadvised in this case):
import functools as ft
print( ft.reduce(lambda x, y: x + ':' + y, list_chars) )
