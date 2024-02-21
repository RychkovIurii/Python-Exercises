fin = open('input.txt', 'r', encoding='utf8')
a9 = []
a10 = []
a11 = []
for line in fin:
    line = list(line.split())
    if line[-2] == '9':
        a9.append(int(line[-1]))
    elif line[-2] == '10':
        a10.append(int(line[-1]))
    elif line[-2] == '11':
        a11.append(int(line[-1]))
a9.sort()
a10.sort()
a11.sort()
x9 = a9.index(max(a9))
x10 = a10.index(max(a10))
x11 = a11.index(max(a11))
print(a9[x9 - 1], a10[x10 - 1], a11[x11 - 1])
fin.close()
