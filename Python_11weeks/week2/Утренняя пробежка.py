x = int(input())
y = int(input())
c = 1
while x < y:
    x = x + 0.1 * x
    c = c + 1
print(c)
