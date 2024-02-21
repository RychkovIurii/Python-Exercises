s = str(input())
s = s[1:]
x = len(s)
y = 2
while x >= 1:
    s = s[:y] + s[y+1:]
    x = x - 1
    y = y + 2
print(s)
