def exp(x, y):
    x, y = float(x), int(y)
    res = 1
    for i in range(abs(y) - 1):
        res *= x
    return 1 / res


print(exp(2, -3))


