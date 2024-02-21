c0 = int(input("any non-negative and non-zero integer number:"))
counter = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        print(int(c0))
        counter += 1
    elif c0 % 2 != 0:
        c0 = 3* c0 + 1
        print(int(c0))
        counter += 1

print("steps = ", counter)