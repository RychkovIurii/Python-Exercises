import math


def IsPrime(n):
    k = 2
    while n % k != 0 and k <= math.sqrt(n):
        k += 1
    if k > math.sqrt(n):
        return True
    return False


n = int(input())
if IsPrime(n) is True:
    print('YES')
else:
    print('NO')
