numList = list(map(int, input().split()))
n = int(input())
place = 1
for i in range(len(numList)):
    if numList[i] >= n:
        place += 1
print(place)
