v1 = int(input())
g1 = int(input())
v2 = int(input())
g2 = int(input())
if g2 <= g1 or (v1 + g1) % 2 != (v2 + g2) % 2:
    print('NO')
else:
    if v1 - (g2 - g1) <= v2 <= v1 + (g2 - g1):
        print('YES')
    else:
        print('NO')
