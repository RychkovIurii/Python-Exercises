fin = open('input.txt', 'r', encoding='utf8')
a9 = []
a10 = []
a11 = []
for line in fin:
    line = list(line.split())
    if line[2] == '9':
        a9.append(int(line[3]))
    elif line[2] == '10':
        a10.append(int(line[3]))
    elif line[2] == '11':
        a11.append(int(line[3]))

print(sum(a9) / len(a9), sum(a10) / len(a10), sum(a11) / len(a11))
