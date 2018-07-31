import os, sys


def conv_to_int(x):
    try:
        x = float(x)
    except ValueError:
        print("Error: Unrecognizable number. Exiting")
        sys.exit()
    return x


ops_connues = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        }

opnd1 = input("Entrer l'operande 1:")
opnd1 = conv_to_int(opnd1)

optn = input("Entrez l'operation '+', '-', '*', '/' :")
if optn not in ops_connues:
    print("Error: Unrecognizable operation. Exiting")
    sys.exit()

opnd2 = input("Entrez l'operande 2:")
opnd2 = conv_to_int(opnd2)
if (optn == '/') and (opnd2==0):
    print("Error: Cannot divide by 0. Exiting")
    sys.exit()

result = ops_connues[optn](opnd1, opnd2)
print()
print("Result: ", result)
