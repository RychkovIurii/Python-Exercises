a, b, c = float(input()), float(input()), float(input())
discriminant = b ** 2 - 4 * a * c
if discriminant == 0:
    x = -b / (2 * a)
    print(x)
elif discriminant > 0:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(('{0:.6f}'.format(x1)), ('{0:.6f}'.format(x2)))
