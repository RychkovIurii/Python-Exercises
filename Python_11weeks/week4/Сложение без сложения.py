def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return sum(a + 1, b - 1)
    if a < b:
        return sum(a - 1, b + 1)


a = int(input())
b = int(input())
print(sum(a, b))
