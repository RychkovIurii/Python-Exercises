n = int(input())
x = float(input())
a = float(input())
result = a
while n > 0 and n < 20:
    a = float(input())
    result *= x
    result += a
    n = n - 1
print(result)
