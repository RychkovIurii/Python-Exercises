p, x, y = int(input()), int(input()), int(input())
sumKop1 = 100 * x + y
percent = p / 100 * sumKop1
sumKop2 = sumKop1 + percent
rub = int(sumKop2 // 100)
kop = int(sumKop2 % 100)
print(rub, kop)
