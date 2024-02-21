n = int(input())
if n % 10 == 1 and n != 11:
    print(n, ' korova', sep='')
elif 2 <= n % 10 <= 4 and (10 > n or n > 20):
    print(n, ' korovy', sep='')
else:
    print(n, ' korov', sep='')
