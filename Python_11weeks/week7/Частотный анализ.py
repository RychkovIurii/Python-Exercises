fin = open('input.txt')
words = dict()
for i in fin.read().split():
    if i in words:
        words[i] = words[i] + 1
    else:
        words[i] = 1
print(*sorted(words, key=lambda x: (-words[x], x)), sep='\n')
