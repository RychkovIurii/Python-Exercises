fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
allStudents = []
for line in fin:
    oneStudent = []
    line = list(line.split())
    oneStudent.append(line[0])
    oneStudent.append(line[1])
    oneStudent.append(line[3])
    allStudents.append(oneStudent)
allStudents.sort()
for i in allStudents:
    print(*i, file=fout)
fin.close()
fout.close()
