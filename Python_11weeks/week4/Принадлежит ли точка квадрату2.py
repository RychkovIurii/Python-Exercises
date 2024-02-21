x1, y1 = float(input()), float(input())


def IsPointInSquare(x1, y1):
    return abs(x1) + abs(y1) <= 1


if IsPointInSquare(x1, y1):
    print('YES')
else:
    print('NO')
