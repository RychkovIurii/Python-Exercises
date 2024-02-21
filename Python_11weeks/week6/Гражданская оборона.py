n = int(input())  # количество селений
sTepm = list(map(int, input().split()))
s = []  # позиция селения и его номер в исходном списке
for i in range(n):
    s.append((sTepm[i], i + 1))
s.sort()

m = int(input())  # количество бомбоубежищ
bTemp = list(map(int, input().split()))
b = []  # позиция бомб и его номер в исходном списке
for i in range(m):
    b.append((bTemp[i], i + 1))
b.sort()
# print(s)
# print(b)
result = [0] * n
count = 0
for i in range(0, n):
    dist = s[i][0] + b[0][0]
    j = count
    while j < m and abs(s[i][0] - b[j][0]) < dist:
        if abs(s[i][0] - b[j][0]) < dist:
            dist = abs(s[i][0] - b[j][0])
            result[s[i][1] - 1] = b[j][1]
            count = j
        j += 1
print(*result)
