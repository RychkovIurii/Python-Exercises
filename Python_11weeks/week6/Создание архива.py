s, n = list(map(int, input().split()))
# s - размер свободного места
# n- число пользователей
numList = []
for _ in range(1, n + 1):
    size = int(input())  # объем данных каждого
    numList.append(size)
count = 0
sum = 0
for i in sorted(numList):
    if i <= s and sum + i <= s:
        count += 1
        sum += i
print(count)
