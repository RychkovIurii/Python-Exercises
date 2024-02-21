s = str(input())
x = int(s.find('h'))
y = int(s.rfind('h'))
print(s[: x] + s[y+1:])
