n = int(input())
x = 10 ** n
y = x // 10
for i in range(x - 1, y - 1, -2):
    print(i, end=' ')
