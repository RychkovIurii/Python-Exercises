n, m = map(int, input().split())
anna = set()
boris = set()
for _ in range(n):
    color = int(input())
    anna.add(color)
for _ in range(m):
    color = int(input())
    boris.add(color)
print(len(anna & boris))
print(*sorted(anna & boris))
print(len(anna - boris))
print(*sorted(anna - boris))
print(len(boris - anna))
print(*sorted(boris - anna))
