n = int(input())
listReal = []
listTemp = []
for i in range(1, n + 1):
    listReal.append(i)
for i in range(n - 1):
    listTemp.append(int(input()))
for i in range(n):
    if listReal[i] not in listTemp:
        print(listReal[i])
