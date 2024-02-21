fin = open('input.txt', 'r', encoding='utf8')
n = int(fin.readline())
maxSet = set(range(1, n + 1))
realSet = set()
for line in fin:
    if line.strip() == 'HELP':
        print(*sorted(maxSet))
    elif line.strip() == 'YES':
        maxSet &= realSet
    elif line.strip() == 'NO':
        maxSet -= realSet
    else:
        realSet = set(map(int, line.split()))
