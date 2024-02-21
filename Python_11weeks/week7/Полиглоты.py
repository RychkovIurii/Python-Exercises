n = int(input())
lang = set()
oneLang = set()
for i in range(n):
    countL = int(input())
    temp = set()
    for j in range(countL):
        temp.add(input())
    oneLang |= temp
    if i == 0:
        lang = temp
    else:
        lang &= temp
print(len(lang))
for x in lang:
    print(x)
print(len(oneLang))
for y in oneLang:
    print(y)
