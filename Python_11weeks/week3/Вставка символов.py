s = str(input())
x = len(s)
while x >= 2:
    s = s[:x-1] + '*' + s[x-1:]
    x = x - 1
print(s)
