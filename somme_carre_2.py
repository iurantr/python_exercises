def somme_carre_2(x1, x2, x3=12, x4=1):
    """
    :param x1: float
    :param x2: float
    :param x3: float
    :param x4: float != 0
    :return: x1^2 + x2^2 + x3^2 + x4^2
    """

    if (x4 == 0):
        print("x4 shouldn't be == 0")
        return -2
    ans = (x1 ** 2 + x2 ** 2 + x3 ** 2) / (x4 ** 2)
    return ans


print(somme_carre_2(1, 2, 3, 4))
print(somme_carre_2(1, 2))
print(somme_carre_2(1, 2, 3))
print(somme_carre_2(1, 2, 3, 0))
