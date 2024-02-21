fin = open('input.txt', 'r', encoding='utf8')
myList = list()
for n in fin:
    n = n.strip().replace('-', '')
    n = n.replace('(', '').replace(')', '')
    n = n.replace('+7', '8')
    if len(n) == 7:
        n = '8495' + n
    myList.append(n)
for i in myList[1:]:
    if i == myList[0]:
        print("YES")
    else:
        print('NO')
fin.close()
