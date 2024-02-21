n = int(input())
count = 1
sumseq = count ** 2
while count < n:
    count += 1
    sumseq += count ** 2
print(sumseq)
