a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if d - a >= 0 >= b - e or d - b >= 0 >= a - e:
    print('YES')
elif d - c >= 0 >= a - e or d - a >= 0 >= c - e:
    print('YES')
elif d - c >= 0 >= b - e or d - b >= 0 >= c - e:
    print('YES')
else:
    print('NO')
