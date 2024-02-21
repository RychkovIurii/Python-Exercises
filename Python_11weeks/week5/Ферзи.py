n = 8
x = []
y = []
for i in range(n):
    x1, y1 = [int(s) for s in input().split()]
    x.append(x1)
    y.append(y1)
ans = 1
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j]:
            ans = 0
        if abs(x[i] - x[j]) == abs(y[i] - y[j]):
            ans = 0
if ans == 1:
    print('NO')
else:
    print('YES')
