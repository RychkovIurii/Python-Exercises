from math import sqrt


def onlySquare():
    n = int(input())
    if n != 0:
        if int(sqrt(n)) ** 2 == n:
            onlySquare()
            print(n, end=' ')
            return True
        else:
            return onlySquare()
    else:
        return False


if onlySquare():
    print()
else:
    print(0)
