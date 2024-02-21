numList = list(map(int, input().split()))
xPrev = numList[0]
for x in numList:
    if x > xPrev:
        print(x, end=' ')
        xPrev = x
    else:
        xPrev = x
