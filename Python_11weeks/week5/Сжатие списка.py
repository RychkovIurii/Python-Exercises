numList = list(map(int, input().split()))
l = len(numList) - 1
while l >= 0:
        if numList[l] == 0:
            numList.append(0)
            numList.pop(l)
        l -= 1
print(*numList)
