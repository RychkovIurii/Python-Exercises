fin = open('input.txt', 'r', encoding='utf8')
myDict = dict()
cities = []
n = int(fin.readline())
for i in range(n):
    myList = list(fin.readline().split())
    for i in myList[1:]:
        myDict[i] = myList[0]
m = int(fin.readline())
for i in range(m):
    city = fin.readline().strip()
    cities.append(city)
for i in cities:
    print(myDict[i])
fin.close()
