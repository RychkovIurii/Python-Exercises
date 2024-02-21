a = list(map(int, input().split()))


def IsAscending(a):
    i = 1
    while i < len(a):
        if a[i] <= a[i - 1]:
            return 'NO'
        else:
            i += 1
    return 'YES'


print(IsAscending(a))
