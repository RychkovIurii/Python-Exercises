numList = list(map(int, input().split()))
for i in range(len(numList)):
    if i % 2 != 0:
        numList[i], numList[i - 1] = numList[i - 1], numList[i]
print(*numList)
