numList = list(map(int, input().split()))
numList1 = numList.copy()
numList2 = numList.copy()
plus = 1
minus = 1
min1 = min(numList)
numList1.pop(numList.index(min(numList)))
min2 = min(numList1)
max1 = max(numList)
numList2.pop(numList.index(max(numList)))
max2 = max(numList2)
if max2 * max1 >= min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)
