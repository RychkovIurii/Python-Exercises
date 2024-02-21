def gcd(a, b):
    if a == 0 or b == 0:
        return 0
    elif a % b == 0 or b % a == 0:
        return min(a, b)
    if a > b:
        return gcd(b, a % b)
    elif a < b:
        return gcd(a, b % a)


a = int(input())
b = int(input())
print(gcd(a, b))
