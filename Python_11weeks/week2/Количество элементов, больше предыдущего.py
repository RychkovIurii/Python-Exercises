now = int(input())
count = 0
while now != 0:
    newNow = int(input())
    if newNow > now:
        count += 1
    now = newNow
print(count)
