def lagrange(k, l, m):
    b = int(k ** (1 / l))
    if k - b ** l == 0:
        return str(b)
    if m == 1:
        return 0
    while lagrange(k - b ** l, l, m - 1) == 0:
        b -= 1
        if b <= 0:
            return 0
    return str(b) + ' ' + lagrange(k - b ** l, l, m - 1)


n = int(input())
print(lagrange(n, 2, 4))
