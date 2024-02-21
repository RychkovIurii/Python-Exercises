a = int(input())
b = int(input())
for x in range(a, b + 1):
    x1 = x // 1000
    x2 = x % 1000 // 100
    x3 = x % 100 // 10
    x4 = x % 10
    if x1 == x4 and x2 == x3:
        print(x)
