numList = list(map(int, input().split()))
newList = []
for i in numList:
    if i not in newList:
        newList.append(i)
print(len(newList))
