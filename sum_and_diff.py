def sum_prod_and_diff(x1, x2, x3):
    """Return the sum and the difference of the parameters"""
    s_x = x1 + x2 + x3
    m_x = x1 * x2 * x3
    d_x = x1 - x2 - x3

    return s_x, m_x, d_x


print(sum_prod_and_diff(13, 23, 32))

x, y, z = sum_prod_and_diff(13, 23, 32)

print(x)
print(y)
print(z)
