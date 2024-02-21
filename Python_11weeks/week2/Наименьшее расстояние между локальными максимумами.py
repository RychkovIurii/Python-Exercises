x = 1
i = 0
V1 = 1
V2 = 0
V3 = 0
max1_n = 0
max2_n = 0
Res = 1000000
while V1 != 0:
    i += 1
    V3 = V2
    V2 = V1
    V1 = int(input())
    if i > 2 and V2 > V1 and V2 > V3 and V1 != 0:
        max2_n = max1_n
        max1_n = i
        if (max1_n > 0) and (max2_n > 0) and (max1_n - max2_n < Res):
            Res = max1_n - max2_n
if Res == 1000000:
    Res = 0
print(Res)
