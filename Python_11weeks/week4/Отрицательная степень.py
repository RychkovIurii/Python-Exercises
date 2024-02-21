def power(a, n):
    k = 1
    m = a
    if a == 0:
        return 0
    elif n == 0:
        return 1
    elif n > 0:
        while k != n:
            m = m * a
            k = k + 1
        return m
    elif n < 0:
        while k != n:
            m = m / a
            k += -1
    return m


a = float(input())
n = int(input())
print(power(a, n))
