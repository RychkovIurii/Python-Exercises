now = int(input())
maxNum = now
match = 1
while now != 0:
    now = int(input())
    if now != 0 and now > maxNum:
        maxNum = now
        match = 1
    elif now == maxNum:
        match = match + 1
print(match)
