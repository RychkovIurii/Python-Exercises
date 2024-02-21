numList = list(map(int, input().split()))
x = []
for i in numList:
    if numList.count(i) == 1:
        x.append(i)
print(*x)
