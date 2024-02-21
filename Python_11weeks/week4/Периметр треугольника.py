import math

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
a = b = c = d = 0


def distance(a, b, c, d):
    return math.sqrt((c - a) ** 2 + (d - b) ** 2)


dist1 = distance(x1, y1, x2, y2)
dist2 = distance(x1, y1, x3, y3)
dist3 = distance(x3, y3, x2, y2)
p = dist1 + dist2 + dist3
print(p)
