n, k = map(int, input().split())
myList = set()
saList = set(range(6, n + 1, 7))
suList = set(range(7, n + 1, 7))
noWork = saList | suList
for i in range(k):
    a, b = map(int, input().split())
    for x in range(a, n + 1, b):
        myList.add(x)
print(len(myList - noWork))
