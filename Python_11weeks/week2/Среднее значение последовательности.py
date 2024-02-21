now = int(input())
sumSeq = now
count = 0
while now != 0:
    now = int(input())
    sumSeq = sumSeq + now
    count += 1
print(sumSeq / count)
