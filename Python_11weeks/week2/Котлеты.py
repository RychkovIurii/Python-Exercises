k = int(input())
m = int(input())
n = int(input())
if n <= k:
    time = 2 * m
elif n * 2 % k == 0:
    time = m * (n * 2 // k)
else:
    time = m * (1 + (n * 2 // k))
print(time)
