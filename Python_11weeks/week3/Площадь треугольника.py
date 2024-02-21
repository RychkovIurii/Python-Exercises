a = float(input())
b = float(input())
c = float(input())
d = 0.5
p = (a + b + c) * d
s = (p * (p - a) * (p - b) * (p - c)) ** d
if s % 2 == 0:
    print(int(s))
else:
    print('{0:.6f}'.format(s))
