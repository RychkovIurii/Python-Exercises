numList = list(map(int, input().split()))
a, b = min(numList), max(numList)
c = numList.index(b)
d = numList.index(a)
numList[c], numList[d] = numList[d], numList[c]
print(*numList)
