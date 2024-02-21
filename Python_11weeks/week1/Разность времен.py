h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
moment1 = 3600 * h1 + 60 * m1 + s1
moment2 = 3600 * h2 + 60 * m2 + s2
x = moment2 - moment1
print(x)
