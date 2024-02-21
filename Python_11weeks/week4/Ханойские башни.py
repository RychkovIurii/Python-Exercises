def rec(n, x, y):
    if n == 1:
        print('1', x, y)
    else:
        z = 6 - x - y
        rec(n - 1, x, z)
        print(n, x, y)
        rec(n - 1, z, y)


n = int(input())
rec(n, 1, 3)
