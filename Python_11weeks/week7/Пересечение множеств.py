n = set(map(int, input().split()))
m = set(map(int, input().split()))
print(*sorted(list(n & m)))
