x, y = float(input()), float(input())


def xor(x, y):
    return x + y == 1


if xor(x, y):
    print('1')
else:
    print('0')
