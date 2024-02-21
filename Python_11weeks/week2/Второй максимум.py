now = int(input())
maxNum = now
maxNum2 = 0
while now != 0:
    now = int(input())
    if now != 0 and now > maxNum:
        maxNum2 = maxNum
        maxNum = now
    elif now != 0 and now > maxNum2:
        maxNum2 = now
print(maxNum2)
