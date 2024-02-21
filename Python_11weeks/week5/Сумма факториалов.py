n = int(input())
fact = n
for i in range(n - 1, 0, -1):
    fact = i * (1 + fact)
print(fact)
