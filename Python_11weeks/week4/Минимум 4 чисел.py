a, b = int(input()), int(input())
c, d = int(input()), int(input())


def min4(a, b, c, d):
    return min(min(min(a, b), c), d)


print(min4(a, b, c, d))
