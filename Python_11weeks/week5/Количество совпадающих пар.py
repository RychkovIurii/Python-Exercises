numList = list(map(int, input().split()))
pair = 0
for i in range(len(numList)):
    for x in range(i + 1, len(numList)):
        if numList[i] == numList[x]:
            pair += 1
print(pair)
