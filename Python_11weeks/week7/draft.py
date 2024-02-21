inFile = open("input.txt", "r", encoding="utf8")
n, line = int(inFile.readline()), inFile.readline()[:-1]
mySet = set(range(1, n + 1))
while line.upper() != "HELP":
    line = mySet & set(map(int, line.split()))
    if len(line) > len(mySet) // 2:
        print("YES")
        mySet -= mySet - line
    else:
        print("NO")
        mySet -= line
    line = inFile.readline()[:-1]
inFile.close()
print(*sorted(list(mySet)))
