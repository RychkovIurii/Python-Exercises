A = map(int, input().split())


def CountSort(A):
    points = [0] * 101
    for i in A:
        points[i] += 1
    for point in range(len(points)):
        print((str(point) + ' ') * points[point], end='')


CountSort(A)
