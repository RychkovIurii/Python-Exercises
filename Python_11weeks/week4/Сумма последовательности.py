def fibo():
    n = int(input())
    if n == 0:
        return 0
    return n + fibo()


print(fibo())
