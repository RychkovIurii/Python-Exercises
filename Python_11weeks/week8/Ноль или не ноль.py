print(
    sum(
        map(
            lambda x: x == 0,
            list(
                map(
                    int,
                    open('input.txt')
                        .read()
                        .split()
                )
            )
        )
    )
)

