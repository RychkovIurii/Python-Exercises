x, y, x1, y1 = map(int, input().split())
if x > y:
    x, y = y, x
if x1 > y1:
    x1, y1 = y1, x1
a = set(range(x, y + 1))
b = set(range(x1, y1 + 1))
c = a & b
print(len(c))
