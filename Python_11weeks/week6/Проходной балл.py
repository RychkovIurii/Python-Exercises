fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
allStudents = []  # поступившие
k = int(fin.readline())
for line in fin:
    line = list(line.split())
    m1 = int(line[-3])
    m2 = int(line[-2])
    m3 = int(line[-1])
    if m1 >= 40 <= m2 \
            and m3 >= 40:
        allStudents.append(m1 + m2 + m3)
allStudents.sort(reverse=True)
if len(allStudents) <= k:
    print(0, file=fout)
elif allStudents[k] == allStudents[k - 1]:
    ball = k - 1
    while ball > 0 and \
            allStudents[ball - 1] == allStudents[ball]:
        ball = ball - 1
    if ball == 0:
        print(1, file=fout)
    else:
        print(allStudents[ball - 1], file=fout)
else:
    print(allStudents[k - 1], file=fout)
fin.close()
fout.close()
