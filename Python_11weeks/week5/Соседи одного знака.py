numList = list(map(int, input().split()))
for i in range(1, len(numList)):
    if numList[i] > 0 and numList[i - 1] > 0:
        print(numList[i - 1], numList[i])
        break
    elif numList[i] < 0 and numList[i - 1] < 0:
        print(numList[i - 1], numList[i])
        break
