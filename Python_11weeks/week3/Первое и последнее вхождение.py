s = str(input())
b = s[::-1]
if s.find('f') == -1:
    print()
elif s.find('f') == (len(s) - b.find('f') - 1):
    print(s.find('f'))
else:
    print(s.find('f'))
    print(len(s) - b.find('f') - 1)
