n = int(input())
numList = list(map(int, input().split()))
x = int(input())
result = numList[0]
for i in numList:
    if abs(i-x) < abs(result - x):
        result = i
print(result)
