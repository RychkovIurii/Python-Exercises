from functools import reduce

print(
    reduce(
        lambda rec, x: rec * (x ** 5),
        map(
            int,
            input().split()),
        1
    )
)
