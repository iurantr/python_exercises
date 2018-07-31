def somme_carre(x1, x2, x3, x4):
    """
    :param x1: float
    :param x2: float >= 0
    :param x3: float
    :param x4: float
    :return: x1^2 + x2^2 + x3^2 + x4^2
    """

    if (x2<0):
        ValueError("x2 should be >= 0")
        return -1
    ans = x1**2 + x2**2 + x3**2 + x4**2
    return ans


print(somme_carre(1, 2, 3, 4))
print(somme_carre(-1, 2, 3, 4))
print(somme_carre(1, -2, 3, 4))
print(somme_carre(1, 2, -3, 4))




