n = int(input())
n1 = n
countNum = 1
countNumMax = 1
while n != 0:
    n = int(input())
    if n == n1:
        countNum += 1
        if countNum > countNumMax:
            countNumMax = countNum
    elif n != n1:
        countNum = 1
        n1 = n
print(countNumMax)
