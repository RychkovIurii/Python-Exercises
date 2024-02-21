fin = open('input.txt', 'r', encoding='utf8')
p = dict()
for line in fin:
    s = line.split()
    p[s[0]] = p.get(s[0], 0) + int(s[-1])
for i in sorted(p):
    print(i, p[i])
fin.close()
