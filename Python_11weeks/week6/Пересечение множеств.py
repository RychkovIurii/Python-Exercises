a = list(map(int, input().split()))
b = list(map(int, input().split()))


def intersection(a, b):
    iA = 0
    iB = 0
    x = []
    while iA < len(a) and iB < len(b):
        if a[iA] == b[iB]:
            x.append(a[iA])
            iA += 1
            iB += 1
        elif a[iA] < b[iB]:
            iA += 1
        elif a[iA] > b[iB]:
            iB += 1
    return x


print(*intersection(a, b))
