numList = list(map(int, input().split()))
x = numList[0]
y = 0
for i in range(1, len(numList)):
    if numList[i] > x:
        x = numList[i]
        y = i
print(x, y)
