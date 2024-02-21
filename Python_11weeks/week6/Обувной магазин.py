size = int(input())
a = sorted(set(list(map(int, input().split()))))
pair = []
for i in a:
    if i - size == 0 or i - size >= 3:
        pair.append(i)
        size = i
print(len(pair))
