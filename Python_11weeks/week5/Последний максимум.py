numList = list(map(int, input().split()))
y1 = max(numList)
y2 = 0
for x in range(len(numList)):
    if numList[x] == y1:
        y2 = x
print(y1, y2)
