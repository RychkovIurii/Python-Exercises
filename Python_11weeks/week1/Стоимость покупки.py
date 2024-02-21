a = int(input())
b = int(input())
n = int(input())
kop = (n * b) % 100
rub = ((n * b) // 100 + n * a)
print(rub, kop)
