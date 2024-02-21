n, k = map(int, input().split())
hit = []
for _ in range(k):
    l, r = map(int, input().split())
    for x in range(l, r + 1):
        hit.append(x)
for y in range(1, n + 1):
    if y not in hit:
        print('I', end='')
    else:
        print('.', end='')
