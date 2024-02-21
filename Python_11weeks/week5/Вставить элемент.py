numList = input().split()
k, c = list(map(int, input().split(' ')))
numList.append(c)
l = len(numList)
while l - 1 > k:
    numList[l - 1], numList[l - 2] = numList[l - 2], numList[l - 1]
    l = l - 1

print(*numList)
