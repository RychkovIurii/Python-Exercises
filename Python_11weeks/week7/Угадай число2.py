fin = open('input.txt', 'r', encoding='utf8')
n, line = int(fin.readline()), fin.readline()[:-1]
maxSet = set(range(1, n + 1))
while line.upper() != 'HELP':
    line = maxSet & set(map(int, line.split()))
    if len(line) > len(maxSet) // 2:
        print("YES")
        maxSet -= maxSet - line
    else:
        print("NO")
        maxSet -= line
    line = fin.readline()[:-1]
print(*sorted(list(maxSet)))
fin.close()
