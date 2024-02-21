numList = input().split()
k = int(input())
l = len(numList)
while k < l - 1:
    numList[k], numList[k+1] = numList[k+1], numList[k]
    k += 1
numList.pop()
print(*numList)
