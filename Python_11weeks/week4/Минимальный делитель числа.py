import math

n = float(input())


def MinDivisor(n):
    k = 2
    while n % k != 0:
        k += 1
        if k > math.sqrt(n):
            k = n
    return int(k)


print(MinDivisor(n))
