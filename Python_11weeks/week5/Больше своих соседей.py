numList = list(map(int, input().split()))
y = 0
for i in range(1, len(numList) - 1):
    if numList[i - 1] < numList[i] and numList[i + 1] < numList[i]:
        y += 1
print(y)
