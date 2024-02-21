a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b:
    if a >= b and a >= c:
        if a**2 == c**2 + b**2:
            print('rectangular')
        elif a**2 < c**2 + b**2:
            print('acute')
        elif a**2 > c**2 + b**2:
            print('obtuse')
    elif b >= a and b >= c:
        if b**2 == a**2 + c**2:
            print('rectangular')
        elif b**2 < a**2 + c**2:
            print('acute')
        elif b**2 > a**2 + c**2:
            print('obtuse')
    elif c >= a and c >= b:
        if c**2 == a**2 + b**2:
            print('rectangular')
        elif c**2 < a**2 + b**2:
            print('acute')
        elif c**2 > a**2 + b**2:
            print('obtuse')
else:
    print('impossible')
