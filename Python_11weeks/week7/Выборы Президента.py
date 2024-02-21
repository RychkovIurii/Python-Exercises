fin = open('input.txt', 'r', encoding='utf8')
fout = open("output.txt", "w", encoding='utf8')
cand = dict()
for line in fin:
    one = line.strip()
    cand[one] = cand.get(one, 0) + 1
allV = sum(cand.values())
p = sorted(cand, key=lambda x: (-cand[x], x))
if cand[p[0]] > allV / 2:
    print(p[0], file=fout)
else:
    print(p[0], p[1], sep='\n', file=fout)
fin.close()
fout.close()
