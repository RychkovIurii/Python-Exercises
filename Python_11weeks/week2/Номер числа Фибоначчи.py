a = int(input())
f1 = 1
f2 = 1
fSum = f1 + f2
n = 1
while fSum <= a:
    fSum = f1 + f2
    f1 = f2
    f2 = fSum
    n = n + 1
if a % f1 == 0:
    print(n)
if a % f1 != 0:
    print(-1)
