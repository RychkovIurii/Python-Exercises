fin = open('input.txt', 'r', encoding='utf8')
a = fin.read().split()
print(len(set(a)))
fin.close()
