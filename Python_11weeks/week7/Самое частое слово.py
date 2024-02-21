fin = open('input.txt')
myDict = dict()
for i in fin.read().split():
    if i in myDict:
        myDict[i] = myDict[i] + 1
    else:
        myDict[i] = 1
print(sorted(myDict, key=lambda x: (-myDict[x], x))[0])
