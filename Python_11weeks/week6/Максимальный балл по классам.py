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
print(max(a9), max(a10), max(a11))
