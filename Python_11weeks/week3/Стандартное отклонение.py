import math

oneSum = 0
oneSumSquares = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    oneSum += x_i
    oneSumSquares += x_i ** 2
    x_i = int(input())
print(math.sqrt((oneSumSquares - oneSum ** 2 / n) / (n - 1)))
