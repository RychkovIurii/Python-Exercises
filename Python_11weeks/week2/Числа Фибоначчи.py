n = int(input())
f1 = 1
f2 = 1
fSum = 1
x = 0
while x < n-2:
    fSum = f1 + f2
    f1 = f2
    f2 = fSum
    x = x + 1
if n == 0:
    fSum = 0
print(fSum)
