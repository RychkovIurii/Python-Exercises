n = int(input())
myDict = dict()
for _ in range(n):
    a, b = input().split()
    myDict[a] = b
    myDict[b] = a
print(myDict[input()])
