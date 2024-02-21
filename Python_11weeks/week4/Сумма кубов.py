def qubes(k, l):
    if l == 0:
        return 0
    q = int(k ** (1 / 3))
    if q ** 3 == k:
        return str(q ** 3)
    while q > 0:
        if qubes(k - q ** 3, l - 1) != 0:
            return str(q ** 3) + ' ' + qubes(k - q ** 3, l - 1)
        q -= 1
    return 0


k = int(input())
print(qubes(k, 7))
