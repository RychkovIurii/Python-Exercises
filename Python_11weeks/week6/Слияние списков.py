a = list(map(int, input().split()))
b = list(map(int, input().split()))


def merge(a, b):
    iA = 0
    iB = 0
    x = []
    while iA <= len(a) and iB <= len(b):
        if iA == len(a):
            for i in range(iB, len(b)):
                x.append(b[i])
            iA += 1
        elif iB == len(b):
            for i in range(iA, len(a)):
                x.append(a[i])
            iB += 1
        elif iA != len(a) and iB != len(b) and a[iA] <= b[iB]:
            x.append(a[iA])
            iA += 1
        elif iA != len(a) and iB != len(b) and a[iA] >= b[iB]:
            x.append(b[iB])
            iB += 1
    return x


print(*merge(a, b))
