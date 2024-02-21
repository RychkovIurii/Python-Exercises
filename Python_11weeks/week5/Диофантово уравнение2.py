a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
y = 0
for x in range(0, 1001):
    if x != e and (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
        y += 1
print(y)
