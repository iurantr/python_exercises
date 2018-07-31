def sum_of_sqrt(*args):
    """Return the sum of square roots of the parameters"""
    ans = .0
    for x in args:
        ans += x ** 0.5
    return ans


print(sum_of_sqrt(12, 13, 7))

import numpy as np


def basic_statistics(*args):
    """Return average and variance of numbers"""
    print(args)
    return np.mean(args), np.var(args)


print(basic_statistics(1, 2, 3, 4, 5, 6))
print(basic_statistics(1, 2, 3))
print(basic_statistics(1))

print(basic_statistics(10,33,55,71))