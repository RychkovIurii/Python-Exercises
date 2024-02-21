x = int(input())
contNumDecrease = 0
contNumIncrease = 0
contNumMax = 0
now = x
if x != 0:
    contNumDecrease = 1
    contNumIncrease = 1
while x != 0:
    x = int(input())
    if x != 0 and x > now:
        contNumIncrease = contNumIncrease + 1
        if contNumIncrease > contNumMax:
            contNumMax = contNumIncrease
        contNumDecrease = 1
        now = x
    elif x != 0 and x < now:
        contNumDecrease = contNumDecrease + 1
        if contNumDecrease > contNumMax:
            contNumMax = contNumDecrease
        contNumIncrease = 1
        now = x
    elif x != 0 and x == now:
        contNumDecrease = 1
        contNumIncrease = 1
if contNumIncrease > contNumMax:
    contNumMax = contNumIncrease
print(contNumMax)
