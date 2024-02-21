numList = list(map(int, input().split()))
ans = 0
count = 0
for i in numList:
    if numList.count(i) > count:
        count = numList.count(i)
        ans = i
print(ans)
