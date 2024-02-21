numList = list(map(int, input().split()))
lenNumlist = len(numList)
for i in range(lenNumlist // 2):
    numList[i], numList[- 1 - i] = numList[- 1 - i], numList[i]
print(* numList)
