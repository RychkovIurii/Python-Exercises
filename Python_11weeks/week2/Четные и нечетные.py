n1 = int(input())
n2 = int(input())
n3 = int(input())
if (n1 + n2) % 2 != 0:
    print('YES')
elif (n2 + n3) % 2 != 0:
    print('YES')
elif (n1 + n3) % 2 != 0:
    print('YES')
else:
    print('NO')
