p, x, y, k = int(input()), int(input()), int(input()), int(input())
sumKop1 = 100 * x + y
percent = p / 100 * sumKop1
sumKop2 = int(sumKop1 + percent)
n = 1
while n < k:
    sumKop1 = sumKop2
    percent = p / 100 * sumKop1
    sumKop2 = int(sumKop1 + percent)
    n = n + 1
rub = int(sumKop2 // 100)
kop = int(sumKop2 % 100)
print(rub, kop)
