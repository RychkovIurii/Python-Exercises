fin = open('input.txt', 'r', encoding='utf8')
school = [0] * 100
for line in fin:
    line = list(line.split())
    schoolNum = int(line[-2])
    school[schoolNum] += 1
m = max(school)
for i in range(len(school)):
    if school[i] == m:
        print(i, end=' ')
fin.close()
