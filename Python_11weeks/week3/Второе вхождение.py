s = str(input())
x = s.find('f')
y = s[x+1:].find('f')
if x == -1:
    print(-2)
elif y == -1:
    print(-1)
else:
    print(x + y + 1)
