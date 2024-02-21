n1 = int(input())
n2 = 0
while n1 > 0:
    temp = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + temp
print(n2)
