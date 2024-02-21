a, b, c = float(input()), float(input()), float(input())
if a == 0:
    if b == 0 and c == 0:
        print(3)
    if b != 0:
        x3 = (-c / b)
        if x3 == -0.0:
            x3 = 0
        print(1, x3)
    if b == 0 and c != 0:
        print(0)
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        x = -b / (2 * a)
        print(1, x)
    elif discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
            print(2, x1, x2)
        else:
            print(2, x1, x2)
    elif discriminant < 0:
        print(0)
