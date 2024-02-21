a = int(input())
b = int(input())
while a > b and a // b > 1:
    if a % 2 == 0:
        a = a / 2
        print(':2')
    elif a % 2 != 0:
        a = a - 1
        print('-1')
while a != b:
    a = a - 1
    print('-1')
