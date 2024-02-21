numList = list(map(int, input().split()))
y = 0
for x in numList:
    if x > 0:
        y += 1
print(y)
