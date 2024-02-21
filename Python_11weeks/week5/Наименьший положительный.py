numList = list(map(int, input().split()))
xPrev = 1000
for x in numList:
    if xPrev > x > 0:
        xPrev = x
print(xPrev)
