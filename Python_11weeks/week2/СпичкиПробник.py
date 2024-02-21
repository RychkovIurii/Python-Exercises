l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
s1 = r1 - l1 #длина 1спички
s2 = r2 - l2 #длина 2спички
s3 = r3 - l3 #длина 3спички
# if r1 < l2 and (l2 - r1) > s3 and (r2 - l3) < (l2 - r1): # когда спички 2 и 3 пересекаются и отрезок между 1 и 2 больше 3ей спички
#    print('-1')
# elif r1 < l3 and (l3 - r1) > s2 and (r3 - l2) < (l3 - r1): # когда спички 3 и 2 пересекаются и отрезок между 1 и 3 больше 2ей спички
#    print('-1')
# elif r2 < l3 and (l3 - r2) > s1 and (r3 - l1) < (l3 - r2): # когда спички 3 и 1 пересекаются и отрезок между 2 и 3 больше 1ей спички
#    print('-1')
# elif r2 < l1 and (l1 - r2) > s3 and (r1 - l3) < (l1 - r2):# когда спички 1 и 3 пересекаются и отрезок между 2 и 1 больше 3ей спички
#    print('-1')
# elif r3 < l1 and (l1 - r3) > s2 and (r1 - l2) < (l1 - r3): # когда спички 1 и 2 пересекаются и отрезок между 3 и 1 больше 2ей спички
#    print('-1')
# elif r3 < l2 and (l2 - r3) > s1 and (r2 - l1) < (l2 - r3): # когда спички 2 и 1 пересекаются и отрезок между 3 и 2 больше 1ей спички
#    print('-1')

if (r1 >= l2 and r2 >= l3) or (r2 >= l1 and r1 >= l3):
    print(0)
elif (r1 >= l3 and r3 >= l2) or (r3 >= l1 and r1 >= l2):
    print(0)
elif (r3 >= l2 and r2 >= l1) or (r2 >= l3 and r3 >= l1):
    print(0)
elif r1 < l2 and (l2 - r1) <= s3 or r2 < l1 and (l1 - r2) <= s3:
    print(3)
elif r1 < l3 and (l3 - r1) <= s2 or r3 < l1 and (l1 - r3) <= s2:
    print(2)
elif r3 < l2 and (l2 - r3) <= s1 or r2 < l3 and (l3 - r2) <= s1:
    print(1)
elif r1 >= l2 and (l3 - r2) <=