import math

x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())


def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
