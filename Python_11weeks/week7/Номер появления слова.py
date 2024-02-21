fin = open('input.txt')
words = dict()
for line in fin:
    myList = line.split()
    for i in myList:
        if i not in words:
            words[i] = []
        words[i].append(1)
        print(len(words[i]) - 1, end=' ')
fin.close()
