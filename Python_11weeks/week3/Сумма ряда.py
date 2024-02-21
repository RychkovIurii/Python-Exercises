n = int(input())
k = 1
sumSeq = 1 / n ** 2
while n > 1:
    n = n - k
    sumSeq = sumSeq + 1 / n ** 2
print(sumSeq)
