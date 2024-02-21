numList = list(map(int, input().split()))
result = []
for i in numList:
    if i != 0 and i % 2 != 0:
        result.append(i)
print(min(result))
