def gcd(a, b):
    if a == 0 or b == 0:
        return 0
    elif a % b == 0 or b % a == 0:
        return min(a, b)
    if a > b:
        return gcd(b, a % b)
    elif a < b:
        return gcd(a, b % a)


def ReduceFraction(n, m):
    p = int(n / gcd(n, m))
    q = int(m / gcd(n, m))
    return p, q


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
