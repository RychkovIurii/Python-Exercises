x = int(input())
x4 = x % 10
x3 = x % 100 // 10
x2 = x % 1000 // 100
x1 = x // 1000
r = (x1 - x4) * (x1 - x4) + (x2 - x3) * (x2 - x3) + 1
print(r)
