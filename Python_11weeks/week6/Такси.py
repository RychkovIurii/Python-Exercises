km = list(map(int, input().split()))
price = list(map(int, input().split()))
km.sort(reverse=True)
price.sort()
sum = 0
for i in range(len(km)):
    sum += km[i] * price[i]
print(sum)
