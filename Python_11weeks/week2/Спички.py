l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
n1 = 1  # номер спички
n2 = 2
n3 = 3
if l2 < l1:  # сортируем по длине
    (l1, l2) = (l2, l1)
    (r1, r2) = (r2, r1)
    (n1, n2) = (n2, n1)
if l3 < l2:
    (l2, l3) = (l3, l2)
    (r2, r3) = (r3, r2)
    (n2, n3) = (n3, n2)
if l2 < l1:
    (l1, l2) = (l2, l1)
    (r1, r2) = (r2, r1)
    (n1, n2) = (n2, n1)
s1 = r1 - l1  # длина 1спички
s2 = r2 - l2  # длина 2спички
s3 = r3 - l3  # длина 3спички
part1 = l2 - r1  # отрезок между спичками 2 и 1
part2 = l3 - r2  # отрезок между спичками 3 и 2
if (l2 <= r1 and l3 <= r2) or r1 >= l3:
    print(0)
elif s1 < part2 and s3 < part1:
    print(-1)
elif (n1 < n3 and s1 >= part2 > 0) or (n1 < n3 and part2 <= 0 and part1 > 0):
    print(n1)
elif s3 >= part1 > 0:
    print(n3)
elif (n3 < n1 and s3 >= part1 > 0) or (n3 < n1 and part1 <= 0 and part2 > 0):
    print(n3)
elif (s1 >= part2 > 0) or (part2 <= 0 and s1 >= part1 > 0):
    print(n1)
