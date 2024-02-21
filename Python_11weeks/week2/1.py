k = int(input())
m = 0
v = k
counter = 0
while k != 0:
    while v > 0:
        m = m * 10 + v % 10
        v //= 10
    if m == k:
        counter += 1
    m = 0
    k -= 1
    v = k
print(counter)
